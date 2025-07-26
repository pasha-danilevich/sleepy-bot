from typing import cast

from aiogram import types
from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from entity.user.service import UserService


@inject
async def get_user_state(
    dialog_manager: DialogManager,
    service: FromDishka[UserService],
    **kwargs: dict,
) -> dict:
    user = cast(types.user.User, dialog_manager.event.from_user)
    user_have_sr = await service.is_user_have_sleep_records(user.id)
    return {
        "is_first": (
            not user_have_sr
        ),  # он считается новым пользователем, если у него не имеется ни одной записи
        "is_awake": True,
        "is_sleeping": False,
    }
