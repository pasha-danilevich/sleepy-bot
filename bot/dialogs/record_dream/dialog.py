from aiogram_dialog import Dialog, DialogManager

from ...core.routing.auto_register import AutoRegister
from . import handlers
from .state import RecordDreamSG
from .windows import windows


class RecordDreamDialog(AutoRegister):
    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows, on_start=handlers.on_start)

    @staticmethod
    async def start(manager: DialogManager, data: handlers.StartData) -> None:
        await manager.start(state=RecordDreamSG.start, data=dict(data))
