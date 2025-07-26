from typing import Any, Dict, Generic, List, Optional, TypeVar, Union

from pydantic import BaseModel

from .base import TortoisePydanticBridge

REQUEST_DTO = TypeVar('REQUEST_DTO', bound=BaseModel)
RESPONSE_PROTOCOL = TypeVar("RESPONSE_PROTOCOL", bound=BaseModel)

CREAT_DTO = TypeVar('CREAT_DTO', bound=BaseModel)
UPDATE_DTO = TypeVar('UPDATE_DTO', bound=BaseModel)


class Create(TortoisePydanticBridge, Generic[CREAT_DTO, RESPONSE_PROTOCOL]):
    async def create(self, dto: CREAT_DTO) -> RESPONSE_PROTOCOL:
        obj = await self.get_model().create(**dto.model_dump())
        return await self.to_pydantic(obj)


class Retrieve(TortoisePydanticBridge, Generic[RESPONSE_PROTOCOL]):
    async def get_by_id(self, id: int) -> Optional[RESPONSE_PROTOCOL]:
        """Получает запись по ID и возвращает её в виде Pydantic-модели."""
        obj = await self.get_model().get_or_none(id=id)
        if obj is None:
            return None
        return await self.to_pydantic(obj)

    async def get_all(self) -> List[RESPONSE_PROTOCOL]:
        objs = await self.get_model().all()
        return [await self.to_pydantic(obj) for obj in objs]

    async def filter(self, filters: Dict[str, Any]) -> List[RESPONSE_PROTOCOL]:
        objs = await self.get_model().filter(**filters)
        return [await self.to_pydantic(obj) for obj in objs]


class Update(TortoisePydanticBridge, Generic[UPDATE_DTO, RESPONSE_PROTOCOL]):
    async def update(self, filters: Dict[str, Any], dto: UPDATE_DTO) -> int:
        return await self.get_model().filter(**filters).update(**dto.model_dump())

    async def update_and_get(
        self, filters: Dict[str, Any], dto: UPDATE_DTO
    ) -> List[RESPONSE_PROTOCOL]:
        update_count = await self.get_model().filter(**filters).update(**dto.model_dump())

        if update_count > 0:
            objs = await self.get_model().filter(**filters).all()
            return [await self.to_pydantic(obj) for obj in objs]
        return []

    async def update_or_create(
        self, filters: Dict[str, Any], dto: Union[UPDATE_DTO, CREAT_DTO]
    ) -> tuple[RESPONSE_PROTOCOL, bool]:
        obj, is_created = await self.get_model().update_or_create(
            defaults=dto.model_dump(exclude_none=False, exclude_unset=True),
            **filters,
        )
        return await self.to_pydantic(obj), is_created


class Delete(TortoisePydanticBridge):
    async def delete(self, id: int) -> None:
        obj = await self.get_model().get(id=id)
        await obj.delete()
