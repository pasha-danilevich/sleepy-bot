import datetime
from typing import Optional

from tortoise.contrib.pydantic import pydantic_model_creator

from entity.tracker.dto import SleepRecordDTO
from infra.db.repo.crud import CRUDMixin
from infra.db.tables import SleepRecord

SleepRecord_pydantic = pydantic_model_creator(SleepRecord)


class SleepRecordRepo(CRUDMixin[SleepRecordDTO]):
    model = SleepRecord
    pydantic_model = SleepRecord_pydantic

    async def get_recent(self, user_id: int) -> Optional[SleepRecordDTO]:
        obj = await self.model.filter(user_id=user_id).order_by('-created_at').first()

        if obj:
            return await self.to_pydantic(obj)
        return None

    async def filter_by_date(self, user_id: int, date: datetime.date) -> list[SleepRecordDTO]:
        objs = await self.model.filter(
            user_id=user_id,
            wakeup_time__year=date.year,
            wakeup_time__month=date.month,
            wakeup_time__day=date.day,
        )
        return [await self.to_pydantic(obj) for obj in objs]
