from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.text import Const

from bot.dialogs.dreams.calendar.dialog import DreamsDialog

from ..tracking.dialog import TrackingDialog
from . import getters
from .state import HomeSG

windows = [
    Window(
        Const(
            "Каждый день ты можешь отмечать время отхода ко сну и пробуждение.",
            when='~is_first',
        ),
        Const(
            'Как будешь отходить ко сну, затрекай этот момент в "Трекере сна".',
            when='is_awake',
        ),
        Const("Сейчас ты спишь.", when='is_sleeping'),
        Row(
            DreamsDialog().start_button("Ваши сновидения"),
            TrackingDialog().start_button("Трек сна"),
        ),
        getter=getters.get_user_state,
        state=HomeSG.start,
    )
]
