from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram import inject

from bot.dialogs.home.dialog import HomeDialog

router = Router()


@router.message(CommandStart())
@inject
async def start_cmd(message: Message, dialog_manager: DialogManager, home_dialog: FromDishka[HomeDialog]):
    user_id = message.from_user.id
    await home_dialog.start(dialog_manager)
