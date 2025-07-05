from aiogram.fsm.state import State
from aiogram_dialog import Dialog

from .state import TrackingSG
from .windows import windows
from ...core.dialogs.mixins import SimpleStart
from ...core.routing.auto_register import AutoRegister


class TrackingDialog(AutoRegister, SimpleStart):
    @property
    def start_state(self) -> State:
        return TrackingSG.start

    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows)
