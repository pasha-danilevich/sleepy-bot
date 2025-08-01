import datetime
import logging
from typing import Any, Dict, cast

from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from entity.tracker.service import TrackerService

logger = logging.getLogger(__name__)


@inject
async def get_dreams(
    dialog_manager: DialogManager, service: FromDishka[TrackerService], **kwargs: dict
) -> dict:
    user = dialog_manager.event.from_user
    if not user:
        raise ValueError("No User")

    sd = cast(Dict[str, Any], dialog_manager.start_data)
    selected_date: datetime.date = sd['selected_date']
    del sd['selected_date']

    sleep_records = await service.sleep_record_repo.filter_by_date(
        user_id=user.id, date=selected_date
    )

    return {
        "buttons": [(r.id, r.id) for r in sleep_records],
        "dreams_count": len(sleep_records),
    }
