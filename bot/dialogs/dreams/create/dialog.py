from aiogram_dialog import Dialog, DialogManager

from bot.core.routing.auto_register import AutoRegister

from . import handlers
from .state import CreateDreamSG
from .windows import windows


class CreateDreamDialog(AutoRegister):
    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows, on_start=handlers.on_start)

    @staticmethod
    async def start(manager: DialogManager, data: handlers.StartData) -> None:
        await manager.start(state=CreateDreamSG.start, data=dict(data))
