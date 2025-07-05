from aiogram_dialog import Dialog, DialogManager
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from . import handlers
from .state import RecordDreamSG
from .windows import windows
from ...core.routing.auto_register import AutoRegister


class RecordDreamDialog(AutoRegister):
    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows, on_start=handlers.on_start)

    @staticmethod
    async def start(manager: DialogManager, data: handlers.StartData) -> None:
        await manager.start(state=RecordDreamSG.start, data=data)