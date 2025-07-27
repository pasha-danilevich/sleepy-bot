import logging

from .repo import SleepRecordRepo

logger = logging.getLogger(__name__)


class TrackerService:
    def __init__(self, sleep_record_repo: SleepRecordRepo):
        self.sleep_record_repo = sleep_record_repo
