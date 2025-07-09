from typing import Any, Dict, Generic, List, Optional, TypeVar

from pydantic import BaseModel

from .base import BaseRepository

REQUEST_DTO = TypeVar('REQUEST_DTO', bound=BaseModel)
RESPONSE_PROTOCOL = TypeVar("RESPONSE_PROTOCOL")


class Create(BaseRepository, Generic[REQUEST_DTO, RESPONSE_PROTOCOL]):
    async def create(self, dto: REQUEST_DTO) -> RESPONSE_PROTOCOL:
        obj = await self.get_model().create(**dto.model_dump())
        return await self.to_pydantic(obj)


class Retrieve(BaseRepository, Generic[RESPONSE_PROTOCOL]):
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


class Update(BaseRepository, Generic[REQUEST_DTO, RESPONSE_PROTOCOL]):
    async def update(
        self, filters: Dict[str, Any], dto: REQUEST_DTO
    ) -> List[RESPONSE_PROTOCOL]:
        update_count = await self.get_model().filter(**filters).update(**dto.model_dump())

        if update_count > 0:
            objs = await self.get_model().filter(**filters).all()
            return [await self.to_pydantic(obj) for obj in objs]
        return []


class Delete(BaseRepository):
    async def delete(self, id: int) -> None:
        obj = await self.get_model().get(id=id)
        await obj.delete()


# class CRUD(Create[REQUEST_DTO, RESPONSE_PROTOCOL], Retrieve, Update[REQUEST_DTO, RESPONSE_PROTOCOL], Delete):
#     pass
