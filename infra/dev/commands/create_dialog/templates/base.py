GETTERS = """async def get_data(**kwargs) -> dict:
    pass
"""

HANDLERS = """from aiogram_dialog import DialogManager


async def on_start(_, manager: DialogManager) -> None:
    pass
"""

DIALOG = """from aiogram_dialog import Dialog
from .windows import windows


class {name}Dialog(AutoRegister):
    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows)

"""

STATE = """from aiogram.fsm.state import State, StatesGroup


class {name}SG(StatesGroup):
    start = State()
"""

WINDOWS = """from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button, Row, Start
from aiogram_dialog.widgets.text import Const

from .state import {name}SG

windows = [
    Window(
        Const("🏠 Главное меню"),
        state={name}SG.start,
    )
]"""
