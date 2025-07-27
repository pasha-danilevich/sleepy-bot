from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from entity.user.service import UserService


@inject
async def get_sleep_state(
    dialog_manager: DialogManager, service: FromDishka[UserService], **kwargs: dict
) -> dict:
    user = dialog_manager.event.from_user
    if not user:
        raise ValueError('User not found')

    is_awake = await service.is_awake(user.id)

    return {
        'is_awake': is_awake,
        'is_sleeping': not is_awake,
    }
