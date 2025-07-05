from abc import ABC, abstractmethod

from aiogram.fsm.state import State
from aiogram_dialog import DialogManager


class SimpleStart(ABC):
    @property
    @abstractmethod
    def start_state(self) -> State:
        raise NotImplementedError


    async def start(self, manager: DialogManager) -> None:
        await manager.start(self.start_state)