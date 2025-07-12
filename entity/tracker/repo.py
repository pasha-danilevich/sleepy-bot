from tortoise.contrib.pydantic import pydantic_model_creator

from entity.tracker.dto import CreateSleepRecordDTO, SleepRecordProtocol, UpdateSleepRecordDTO
from infrastructure.db.repo.crud import CRUDMixin
from infrastructure.db.tables import SleepRecord, User


class SRWithUser(pydantic_model_creator(SleepRecord)):
    user: pydantic_model_creator(User)


class SleepRecordRepo(
    CRUDMixin[CreateSleepRecordDTO, SleepRecordProtocol, UpdateSleepRecordDTO]
):
    model = SleepRecord
    pydantic_model = SRWithUser
