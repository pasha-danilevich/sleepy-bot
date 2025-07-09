from datetime import datetime
from typing import Optional, Protocol

from pydantic import BaseModel

from infrastructure.db.database import init_db
from infrastructure.db.repo.mixins import Create, Retrieve, Update
from infrastructure.db.tables import SleepRecord


class CreateSleepRecordDTO(BaseModel):
    user_id: int
    bedtime: datetime


class UpdateSleepRecordDTO(BaseModel):
    wakeup_time: datetime
    dream_text: str
    sleep_score: int


class SleepRecordProtocol(Protocol):
    id: int
    user_id: int
    bedtime: datetime
    wakeup_time: Optional[datetime]
    dream_text: Optional[str]
    sleep_score: Optional[int]


class SomeRepo(
    Retrieve[SleepRecordProtocol],
    Create[CreateSleepRecordDTO, SleepRecordProtocol],
    Update[UpdateSleepRecordDTO, SleepRecordProtocol],
):
    model = SleepRecord


async def main():
    # Тестируем
    await init_db()
    repo = SomeRepo()
    record = await repo.get_by_id(1)
    print(record.bedtime)

    dto = CreateSleepRecordDTO(user_id=1, bedtime=datetime.now())
    sleep_record = await repo.create(dto)
    update_dto = UpdateSleepRecordDTO(
        wakeup_time=datetime.now(), dream_text='hahaha', sleep_score=5
    )
    s = await repo.update(filters={'user_id': 1}, dto=update_dto)
    print(s, sleep_record)
    f = await repo.filter({'dream_text': None})
    print(len(f))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
