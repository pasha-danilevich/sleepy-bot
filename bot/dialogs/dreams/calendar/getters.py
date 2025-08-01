import logging

from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from entity.tracker.service import TrackerService

logger = logging.getLogger(__name__)


@inject
async def get_special_dates(
    dialog_manager: DialogManager, service: FromDishka[TrackerService], **kwargs: dict
) -> dict:
    user = dialog_manager.event.from_user
    if not user:
        raise ValueError("No User")

    all_sleep_record = await service.sleep_record_repo.filter({'user_id': user.id})
    special_dates = [sr.wakeup_time.date() for sr in all_sleep_record if sr.wakeup_time]

    return {
        "special_dates": special_dates,
        "is_empty": not bool(len(special_dates)),
    }
