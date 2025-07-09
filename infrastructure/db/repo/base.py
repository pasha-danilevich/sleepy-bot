from typing import Type

from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator
from tortoise.models import Model


class BaseRepository:
    model: Type[Model] = None  # Класс Tortoise модели

    def get_model(self) -> Type[Model]:
        assert (
            self.model is not None
        ), f'{self.__class__.__name__} должен иметь атрибут "model"'
        return self.model

    def get_pydantic_model_creator(self) -> Type[PydanticModel]:
        return pydantic_model_creator(self.model)

    async def to_pydantic(self, obj: Model) -> PydanticModel:
        return await self.get_pydantic_model_creator().from_tortoise_orm(obj)
