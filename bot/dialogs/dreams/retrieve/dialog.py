import datetime

from aiogram_dialog import Dialog, DialogManager

from bot.core.routing.auto_register import AutoRegister

from .state import RetrieveDreamSG
from .windows import windows


class RetrieveDreamDialog(AutoRegister):
    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows)

    @staticmethod
    async def start(manager: DialogManager, selected_date: datetime.date) -> None:
        await manager.start(RetrieveDreamSG.dream, data={'selected_date': selected_date})

    @staticmethod
    async def start_no_dream(manager: DialogManager) -> None:
        await manager.start(RetrieveDreamSG.no_dream)
