from datetime import datetime

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from bot.dialogs.record_dream.dialog import RecordDreamDialog
from entity.tracker.service import TrackerService


@inject
async def start_record_dream(
    _: CallbackQuery, __: Button, manager: DialogManager, dialog: FromDishka[RecordDreamDialog]
) -> None:
    await dialog.start(manager, {'create_date': datetime.now()})


@inject
async def go_to_sleep(
    _: CallbackQuery,
    __: Button,
    manager: DialogManager,
    service: FromDishka[TrackerService],
) -> None:
    user = manager.event.from_user
    if not user:
        raise ValueError('User not found')
    data = {'user_id': user.id, 'bedtime': datetime.now()}
    await service.sleep_record_repo.create(data)
