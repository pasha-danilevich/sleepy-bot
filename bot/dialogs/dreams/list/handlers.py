import logging

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Select
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from entity.tracker.service import TrackerService

logger = logging.getLogger(__name__)


@inject
async def on_dream_select(
    _: CallbackQuery,
    __: Select,
    manager: DialogManager,
    item: str,
    service: FromDishka[TrackerService],
) -> None:
    # data = cast(dict[str, Any], manager.dialog_data)
    # selected_date: datetime.date = sd['selected_date']
    print(item)
    raise NotImplementedError()
