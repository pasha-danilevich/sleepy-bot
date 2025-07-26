import pytest

from entity.tracker.repo import SleepRecordRepo
from entity.user.repo import UserRepo
from entity.user.service import UserService
from infra.db.database import init_db


@pytest.mark.asyncio
async def test_is_user_have_sleep_records():
    await init_db()
    serv = UserService(
        user_repo=UserRepo(),
        sleep_record_repo=SleepRecordRepo(),
    )
    x = await serv.is_user_have_sleep_records(user_id=1)
    print(x)
