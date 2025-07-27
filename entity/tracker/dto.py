from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class SleepRecordDTO(BaseModel):
    id: int
    user_id: int
    bedtime: datetime
    wakeup_time: Optional[datetime]
    dream_text: Optional[str]
    sleep_score: Optional[int]
