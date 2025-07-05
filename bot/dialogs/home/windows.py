from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.text import Const

from ..dreams.dialog import DreamsDialog
from ..tracking.dialog import TrackingDialog
from .state import HomeSG

windows = [
    Window(
        Const("Каждый день ты можешь отмечать время отхода ко сну и пробуждение."),
        Row(
            TrackingDialog().start_button("⏰ Трек сна"),
            DreamsDialog().start_button("Ваши сновидения"),
        ),
        state=HomeSG.start,
    )
]
