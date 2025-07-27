from tortoise.contrib.pydantic import pydantic_model_creator

from entity.tracker.dto import SleepRecordDTO
from infra.db.repo.crud import CRUDMixin
from infra.db.tables import SleepRecord

SleepRecord_pydantic = pydantic_model_creator(SleepRecord)


class SleepRecordRepo(CRUDMixin[SleepRecordDTO]):
    model = SleepRecord
    pydantic_model = SleepRecord_pydantic
