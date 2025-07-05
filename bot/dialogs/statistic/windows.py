from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const

from .state import StatisticSG

windows = [
Window(
        Const("Статистика"),
        state=StatisticSG.start,
    )
]