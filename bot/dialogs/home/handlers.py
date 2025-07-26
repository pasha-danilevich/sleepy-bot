import logging
from typing import Any, cast

from aiogram import types
from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from entity.user.dto import UpdateUserDTO
from entity.user.service import UserService

logger = logging.getLogger(__name__)


@inject
async def on_start(_: Any, manager: DialogManager, service: FromDishka[UserService]) -> None:
    logger.debug('Создаем или обновляем пользователя')
    user = cast(types.user.User, manager.event.from_user)

    user_dto = UpdateUserDTO(
        username=user.username,
        fullname=f'{user.first_name} {user.last_name}',
    )

    await service.repo.update_or_create(filters={'id': user.id}, dto=user_dto)
