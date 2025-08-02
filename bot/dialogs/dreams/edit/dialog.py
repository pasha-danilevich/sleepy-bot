from aiogram.fsm.state import State
from aiogram_dialog import Dialog, DialogManager

from bot.core.routing.auto_register import AutoRegister

from .state import EditDreamSG
from .windows import windows


class EditDreamDialog(AutoRegister):
    @property
    def _start_state(self) -> State:
        return EditDreamSG.edit

    @staticmethod
    def get_dialog() -> Dialog:
        return Dialog(*windows)

    async def start(self, manager: DialogManager, dream_id: int) -> None:
        await manager.start(self._start_state, data={'dream_id': dream_id})
