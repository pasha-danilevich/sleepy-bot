from aiogram.fsm.state import State
from aiogram_dialog import Dialog

from ...core.dialogs.mixins import SimpleStart
from ...core.routing.auto_register import AutoRegister
from . import handlers
from .state import StartSG
from .windows import windows


class StartDialog(AutoRegister, SimpleStart):
    @property
    def _start_state(self) -> State:
        return StartSG.start

    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows, on_start=handlers.on_start)
