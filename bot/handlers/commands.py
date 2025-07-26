from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram import inject

from bot.dialogs.start.dialog import StartDialog

router = Router()


@router.message(CommandStart())
@inject
async def start_cmd(
    message: Message, dialog_manager: DialogManager, dialog: FromDishka[StartDialog]
) -> None:
    await dialog.start(dialog_manager)
