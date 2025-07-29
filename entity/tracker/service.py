import logging
from datetime import datetime, timezone

from .dto import SleepRecordDTO
from .repo import SleepRecordRepo

logger = logging.getLogger(__name__)


class TrackerService:
    def __init__(self, sleep_record_repo: SleepRecordRepo):
        self.sleep_record_repo = sleep_record_repo

    async def wakeup(self, user_id: int) -> SleepRecordDTO:
        recent_sr = await self.sleep_record_repo.get_recent(user_id)
        if not recent_sr:
            raise ValueError(f'Sleep Record Not Exist')

        logger.debug(f"User: {user_id} update sleep record: {recent_sr.id}. Wakeup")
        filters = {'id': recent_sr.id}
        data = {'wakeup_time': datetime.now(timezone.utc)}
        logger.debug(f'{data=}')
        records = await self.sleep_record_repo.update_and_get(filters, data)

        if len(records) > 1:
            logger.warning("To many records updated")
        return records[0]
