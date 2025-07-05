from datetime import datetime

from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from bot.dialogs.record_dream.dialog import RecordDreamDialog


async def on_start(_, manager: DialogManager) -> None:
    pass

@inject
async def start_record_dream(_, __, manager: DialogManager, dialog: FromDishka[RecordDreamDialog]) -> None:
    await dialog.start(manager, {'create_date': datetime.now()})