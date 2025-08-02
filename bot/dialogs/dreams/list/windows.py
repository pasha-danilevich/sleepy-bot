from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel, Group
from aiogram_dialog.widgets.text import Const, Format

from bot.core.widgets.buttons import DynamicButtons

from . import getters, handlers
from .state import DreamsListSG

windows = [
    Window(
        Format("В этот день у вас {dreams_count} записей"),
        Group(
            DynamicButtons(
                on_click=handlers.on_dream_select,
            ),
            width=1,
        ),
        Cancel(Const("Назад")),
        state=DreamsListSG.start,
        getter=[getters.get_dreams],
    ),
]
