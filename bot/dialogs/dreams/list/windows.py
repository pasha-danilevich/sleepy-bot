from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Const, Format

from bot.core.widgets.buttons import DynamicButtons

from . import getters, handlers
from .state import DreamsListSG

windows = [
    Window(
        Format("В этот день вы записал {dreams_count} снов"),
        DynamicButtons(
            on_click=handlers.on_dream_select,
        ),
        Cancel(Const("Назад")),
        state=DreamsListSG.start,
        getter=[getters.get_dreams],
    ),
]
