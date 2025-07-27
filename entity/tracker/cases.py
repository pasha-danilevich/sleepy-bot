from datetime import datetime
from pprint import pprint

from entity.tracker.repo import SleepRecordRepo
from infra.db.database import init_db


async def main() -> None:
    # Тестируем
    await init_db()
    repo = SleepRecordRepo()
    record = await repo.get_by_id(1)
    if record:
        pprint(record.model_dump())
    print('*' * 10)

    sleep_record, is_created = await repo.update_or_create(
        filters={'user_id': 1},
        data={'user_id': 1, 'bedtime': datetime.now()},
    )

    pprint(sleep_record.model_dump())
    print(is_created)
    print('*' * 10)

    s = await repo.update(
        filters={'user_id': 1},
        data={'wakeup_time': datetime.now(), 'dream_text': 'super dream', 'sleep_score': 5},
    )
    pprint(s)
    print('*' * 10)

    f = await repo.filter({'user_id': 1})
    pprint([f.model_dump() for f in f])
    print('*' * 10)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
