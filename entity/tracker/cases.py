from datetime import datetime
from pprint import pprint

from infrastructure.db.database import init_db

from .repo import *


async def main():
    # Тестируем
    await init_db()
    repo = SleepRecordRepo()
    record = await repo.get_by_id(1)
    pprint(record.model_dump())
    print('*' * 10)

    dto = CreateSleepRecordDTO(user_id=1, bedtime=datetime.now())
    sleep_record, is_created = await repo.update_or_create(filters={'user_id': 1}, dto=dto)
    pprint(sleep_record.model_dump())
    print(is_created)
    print('*' * 10)

    update_dto = UpdateSleepRecordDTO(
        wakeup_time=datetime.now(), dream_text='hahaha', sleep_score=5
    )
    s = await repo.update(filters={'user_id': 1}, dto=update_dto)
    pprint(s)
    print('*' * 10)

    f = await repo.filter({'user_id': 1})
    pprint([f.model_dump() for f in f])
    print('*' * 10)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
