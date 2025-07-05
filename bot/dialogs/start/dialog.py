from aiogram.fsm.state import State
from aiogram_dialog import Dialog

from . import handlers
from .windows import windows
from ...core.dialogs.mixins import SimpleStart
from ...core.routing.auto_register import AutoRegister
from .state import StartSG

class StartDialog(AutoRegister, SimpleStart):
    @property
    def start_state(self) -> State:
        return StartSG.start

    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows, on_start=handlers.on_start)

