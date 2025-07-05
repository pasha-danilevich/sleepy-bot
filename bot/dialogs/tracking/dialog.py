from aiogram.fsm.state import State
from aiogram_dialog import Dialog

from ...core.dialogs.mixins import SimpleStart
from ...core.routing.auto_register import AutoRegister
from .state import TrackingSG
from .windows import windows


class TrackingDialog(AutoRegister, SimpleStart):
    @property
    def _start_state(self) -> State:
        return TrackingSG.start

    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows)
