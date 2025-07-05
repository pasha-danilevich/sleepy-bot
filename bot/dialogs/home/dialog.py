from aiogram.fsm.state import State
from aiogram_dialog import Dialog

from bot.core.routing.auto_register import AutoRegister

from ...core.dialogs.mixins import SimpleStart
from .state import HomeSG
from .windows import windows


class HomeDialog(AutoRegister, SimpleStart):
    @property
    def _start_state(self) -> State:
        return HomeSG.start

    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows)
