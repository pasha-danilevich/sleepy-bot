from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from .state import StartSG
from ..home.state import HomeSG

windows = [
    Window(
        Const("Привет! Я помогу тебе улучшить твой сон."),
        Start(Const('Начать'), state=HomeSG.start, id='home'),
        state=StartSG.start,
    )
]