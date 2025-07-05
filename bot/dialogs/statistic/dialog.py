from aiogram.fsm.state import State
from aiogram_dialog import Dialog

from bot.core.routing.auto_register import AutoRegister
from .state import StatisticSG
from .windows import windows
from ...core.dialogs.mixins import SimpleStart


class StatisticDialog(AutoRegister, SimpleStart):
    @property
    def start_state(self) -> State:
        return StatisticSG.start

    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows)
