from aiogram_dialog import DialogManager


async def get_user_state(dialog_manager: DialogManager, **kwargs):
    return {
        "is_first": False,
        "is_awake": True,
        "is_sleeping": False,
    }
