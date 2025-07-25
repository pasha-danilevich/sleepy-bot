import pytest

from entity.tracker.repo import SleepRecordRepo
from infra.db.database import init_db


@pytest.mark.asyncio
async def test_is_user_have_sleep_records():
    await init_db()
    repo = SleepRecordRepo()
    records = await repo.get_all()
    print(records)
