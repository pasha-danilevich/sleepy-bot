import logging

from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from entity.user.dto import UpdateUserDTO
from entity.user.service import UserService

logger = logging.getLogger(__name__)


@inject
async def on_start(_, manager: DialogManager, service: FromDishka[UserService]) -> None:
    logger.debug('Создаем или обновляем пользователя')
    tg_user = manager.event.from_user

    user = UpdateUserDTO(
        username=tg_user.username,
        fullname=f'{tg_user.first_name} {tg_user.last_name}',
    )

    await service.repo.update_or_create(filters={'id': tg_user.id}, dto=user)
