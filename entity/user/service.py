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

        logger.debug("User have sleep records" if is_have else "No sleep records")
        return is_have

    async def is_awake(self, user_id: int) -> bool:
        recent_sr = await self.sleep_record_repo.get_recent(user_id)

        if not recent_sr:
            logger.debug(f"No sleep records found for user {user_id} - considering awake")
            return True

        if recent_sr.wakeup_time:
            logger.debug(
                f"User {user_id} has wakeup time {recent_sr.wakeup_time} - considering awake"
            )
            return True

        logger.debug(
            f"User {user_id} has no wakeup time in recent record - considering asleep"
        )
        return False
