from typing import Type

from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator
from tortoise.models import Model


class TortoisePydanticBridge:
    """
    Мост между Tortoise ORM и Pydantic для конвертации моделей.

    Attributes:
        model: Класс модели Tortoise ORM
        pydantic_model: Опциональный класс Pydantic модели (если None - модель создастся динамически
       с учётом всех связей)
    """

    model: Type[Model] = None
    pydantic_model: Type[PydanticModel] = None

    def get_model(self) -> Type[Model]:
        assert self.model is not None, f'{self.__class__.__name__}: не указана модель'
        return self.model

    def get_pydantic_model(self) -> Type[PydanticModel]:
        """
        Возвращает Pydantic модель:
        - Если pydantic_model задан - возвращает его
        - Если pydantic_model==None - создаёт динамически через pydantic_model_creator
        """
        return (
            self.pydantic_model
            if self.pydantic_model
            else pydantic_model_creator(self.get_model())
        )

    async def to_pydantic(self, obj: Model) -> PydanticModel:
        return await self.get_pydantic_model().from_tortoise_orm(obj)
