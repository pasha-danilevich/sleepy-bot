import logging

from aiogram_dialog import DialogManager, StartMode
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from bot.dialogs.home.dialog import HomeDialog

logger = logging.getLogger(__name__)


@inject
async def on_start(
    _,
    manager: DialogManager,
    home_dialog: FromDishka[HomeDialog],
) -> None:
    logger.info('Создаем или обновляем пользователя в Бд')
    user, is_created = '', False
    if not is_created:
        logger.info('Пользователь есть в БД')
        await home_dialog.start(manager, mode=StartMode.RESET_STACK)
