from aiogram.fsm.state import State
from aiogram_dialog import Dialog

from bot.core.routing.auto_register import AutoRegister

from ...core.dialogs.mixins import SimpleStart
from .state import StatisticSG
from .windows import windows


class StatisticDialog(AutoRegister, SimpleStart):
    @property
    def _start_state(self) -> State:
        return StatisticSG.start

    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows)
