from typing import Generic, Optional, Protocol, Type, TypeVar

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model

from infrastructure.db.database import init_db
from infrastructure.db.tables.sleep_record import SleepRecord

# Типы для дженериков
MODEL = TypeVar("MODEL", bound=Model)
PYDANTIC_MODEL = TypeVar("PYDANTIC_MODEL", bound=BaseModel)
RESPONSE_PROTOCOL = TypeVar("RESPONSE_PROTOCOL")


class BaseRepository(Generic[MODEL, RESPONSE_PROTOCOL]):
    model: Type[MODEL]  # Класс модели (например, SleepRecord)


class Retrieve(BaseRepository[MODEL, RESPONSE_PROTOCOL]):
    async def get_by_id(self, id: int) -> Optional[RESPONSE_PROTOCOL]:
        """Получает запись по ID и возвращает её в виде Pydantic-модели."""
        obj = await self.model.get_or_none(id=id)
        if obj is None:
            return None
        return await pydantic_model_creator(self.model).from_tortoise_orm(obj)


# Пример использования
class SomeDTO(Protocol):
    id: int


class SomeRepo(Retrieve[SleepRecord, SomeDTO]):
    model = SleepRecord


async def main():
    # Тестируем
    await init_db()
    repo = SomeRepo()
    record = await repo.get_by_id(1)  # Тип record: Optional[SomeDTO]
    print(record.id)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
