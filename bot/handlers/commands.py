from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager
from dishka.integrations.aiogram import inject

router = Router()


@router.message(CommandStart())
@inject
async def start_cmd(message: Message, dialog_manager: DialogManager):
    user_id = message.from_user.id

    # Проверяем, есть ли пользователь в БД
    if user_id not in fake_db:
        # Если нет - показываем приветствие
        await dialog_manager.start(MainSG.welcome, mode=StartMode.RESET_STACK)
    else:
        # Если есть - сразу в главное меню
        await dialog_manager.start(MainSG.home, mode=StartMode.RESET_STACK)
