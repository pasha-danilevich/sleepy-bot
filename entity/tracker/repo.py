from datetime import datetime
from typing import Optional, Protocol

from infrastructure.db.base.repo import BaseRepository
from infrastructure.db.database import init_db
from infrastructure.db.tables import SleepRecord
from infrastructure.db.tables.sleep_record import SleepRecordPydantic


class SleepRecordProtocol(Protocol):
    id: int
    user_id: int
    bedtime: datetime
    wakeup_time: Optional[datetime]
    dream_text: Optional[str]
    sleep_score: Optional[int]


class TrackerRepo(BaseRepository[SleepRecordProtocol]):
    def __init__(self) -> None:
        super().__init__(SleepRecord, SleepRecordPydantic)


async def main():
    await init_db()
    repo = TrackerRepo()
    from datetime import datetime

    data = {'user_id': 1, 'bedtime': datetime.now()}
    # print(await repo.create(**data))

    obj = await repo.get_by_id(id=1)

    print(
        obj
    )  # почему, мне типизация не подсказывает какие атрибуты есть у данного объекта, хотя известно, что это SleepRecordPydantic
    print(type(obj))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
