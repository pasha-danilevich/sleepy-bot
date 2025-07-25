import logging

from aiogram_dialog import DialogManager, StartMode
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from bot.dialogs.home.dialog import HomeDialog
from entity.user.service import UserService

logger = logging.getLogger(__name__)


@inject
async def on_start(
    _,
    manager: DialogManager,
    home_dialog: FromDishka[HomeDialog],
    service: FromDishka[UserService],
) -> None:
    logger.debug('Проверяем, если ли user в Бд')
    user = await service.repo.get_by_id(manager.event.from_user.id)
    if user:
        logger.debug('Пользователь есть в БД')
        await home_dialog.start(manager, mode=StartMode.RESET_STACK)
    else:
        logger.debug('Пользователя нет в БД')
