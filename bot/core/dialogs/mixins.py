from abc import ABC, abstractmethod

from aiogram.fsm.state import State
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const


class SimpleStart(ABC):
    @property
    @abstractmethod
    def _start_state(self) -> State:
        raise NotImplementedError

    async def start(self, manager: DialogManager, mode: StartMode = StartMode.NORMAL) -> None:
        await manager.start(self._start_state, mode=mode)

    def start_button(self, btn_text: str) -> Start:
        return Start(
            Const(btn_text), id=f'start_{self.__class__.__name__}', state=self._start_state
        )
