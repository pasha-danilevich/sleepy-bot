from datetime import datetime, timezone
from typing import cast

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from bot.dialogs.dreams.create import CreateDreamDialog
from entity.tracker.service import TrackerService
from entity.tracker.utils import SleepUtils


async def start_record_dream(_: CallbackQuery, __: Button, manager: DialogManager) -> None:
    await CreateDreamDialog().start(manager, {'create_date': datetime.now()})


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

    data = {'user_id': user.id, 'bedtime': datetime.now(timezone.utc)}
    await service.sleep_record_repo.create(data)


@inject
async def on_wakeup(
    _: CallbackQuery,
    __: Button,
    manager: DialogManager,
    service: FromDishka[TrackerService],
) -> None:
    user = manager.event.from_user
    if not user:
        raise ValueError('User not found')

    sleep_record = await service.wakeup(user.id)
    wakeup_time = cast(datetime, sleep_record.wakeup_time)  # wakeup_time только что создано

    manager.dialog_data['sleep_duration'] = SleepUtils.get_sleep_duration(
        bedtime=sleep_record.bedtime,
        wakeup_time=wakeup_time,
    )
