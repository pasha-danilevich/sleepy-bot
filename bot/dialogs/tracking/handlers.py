from datetime import datetime
from typing import Any

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from bot.dialogs.record_dream.dialog import RecordDreamDialog


async def on_start(_: Any, manager: DialogManager) -> None:
    pass


@inject
async def start_record_dream(
    _: CallbackQuery, __: Button, manager: DialogManager, dialog: FromDishka[RecordDreamDialog]
) -> None:
    await dialog.start(manager, {'create_date': datetime.now()})
