from typing import Any, Generic, Optional, Protocol, Type, TypeVar

from pydantic import BaseModel
from tortoise.models import Model

# Тип модели (наследник от Model)
MODEL = TypeVar("MODEL", bound=Model)
PYDANTIC_MODEL = TypeVar("PYDANTIC_MODEL", bound=BaseModel)
RESPONSE_PROTOCOL = TypeVar("RESPONSE_PROTOCOL", bound=Protocol)


class BaseRepository(Generic[RESPONSE_PROTOCOL]):
    def __init__(
        self,
        model: Type[MODEL],
        pydantic_model: Type[PYDANTIC_MODEL],
        response_type: Type[RESPONSE_PROTOCOL],
    ) -> None:
        self.model = model
        self.pydantic_model = pydantic_model

    async def create(self, **kwargs: Any) -> RESPONSE_PROTOCOL:
        """Создание новой записи."""
        return await self.model.create(**kwargs)

    async def get_by_id(self, id: int) -> Optional[RESPONSE_PROTOCOL]:
        """Получение записи по ID."""
        obj = await self.model.get_or_none(id=id)
        if obj is None:
            return None
        return await self.pydantic_model.from_tortoise_orm(obj)
