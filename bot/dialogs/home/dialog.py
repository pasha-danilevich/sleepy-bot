from aiogram.fsm.state import State
from aiogram_dialog import Dialog, StartMode
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from bot.core.routing.auto_register import AutoRegister

from ...core.dialogs.mixins import SimpleStart
from .handlers import on_start
from .state import HomeSG
from .windows import windows


class HomeDialog(AutoRegister, SimpleStart):
    @property
    def _start_state(self) -> State:
        return HomeSG.start

    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows, on_start=on_start)

    def start_button(self, btn_text: str = 'На главную') -> Start:
        return Start(
            Const(btn_text),
            id=f'start_{self.__class__.__name__}',
            state=self._start_state,
            mode=StartMode.RESET_STACK,
        )
