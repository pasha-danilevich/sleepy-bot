
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.text import Const

from .state import HomeSG

from ..tracking.dialog import TrackingDialog

windows = [
    Window(
        Const("Каждый день ты можешь отмечать время отхода ко сну и пробуждение."),
        Row(
            TrackingDialog().start_button('⏰ Трек сна'),
        ),
        state=HomeSG.start,
    )
]
