import logging

from ..tracker.repo import SleepRecordRepo
from .repo import UserRepo

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, user_repo: UserRepo, sleep_record_repo: SleepRecordRepo):
        self.repo = user_repo
        self.sleep_record_repo = sleep_record_repo

    async def is_user_have_sleep_records(self, user_id: int) -> bool:
        records = await self.sleep_record_repo.filter({'user_id': user_id})
        is_have = True if records else False

        logger.debug(f"{len(records)=} поэтому {is_have=}")
        return is_have
