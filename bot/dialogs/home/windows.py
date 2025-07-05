from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const

from .state import HomeSG

windows = [
Window(
        Const("🏠 Главное меню"),
        Row(
            Button(Const("📊 Статистика"), id="stats_btn"),
            Button(Const("⏰ Трек сна"), id="track_btn"),
        ),
        state=HomeSG.start,
    )
]