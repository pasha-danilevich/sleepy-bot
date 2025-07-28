from datetime import datetime, timedelta

import pytest

from entity.tracker.repo import SleepRecordRepo
from entity.tracker.utils import SleepUtils
from infra.db.database import init_db


@pytest.mark.asyncio
async def test_is_user_have_sleep_records():
    await init_db()
    repo = SleepRecordRepo()
    records = await repo.get_all()
    print(records)


@pytest.mark.asyncio
async def test_is_user_have_sleep_records():
    bedtime = datetime(2025, 7, 12, 22, 30)
    wakeup_time = datetime(2025, 7, 13, 6, 45)

    sleep_duration = SleepUtils.get_sleep_duration(bedtime, wakeup_time)

    assert sleep_duration == timedelta(hours=8, minutes=15)

    bedtime = datetime(2025, 7, 12, 22, 30)
    wakeup_time = datetime(2025, 7, 14, 6, 45)
    sleep_duration = SleepUtils.get_sleep_duration(bedtime, wakeup_time)

    assert sleep_duration == timedelta(days=1, hours=8, minutes=15)
    assert sleep_duration == timedelta(hours=32, minutes=15)

    bedtime = datetime(2025, 7, 12, 22, 0, 0)
    wakeup_time = datetime(2025, 7, 12, 22, 0, 5)
    sleep_duration = SleepUtils.get_sleep_duration(bedtime, wakeup_time)
    print(sleep_duration)
    assert sleep_duration == timedelta(seconds=5)


def test_formatter():
    bedtime = datetime(2025, 7, 12, 22, 30, 0)
    wakeup_time = datetime(2025, 7, 13, 7, 45, 3)

    delta = SleepUtils.get_sleep_duration(bedtime, wakeup_time)
    assert SleepUtils.format_timedelta(delta) == "9 часов 15 минут 3 секунды"
