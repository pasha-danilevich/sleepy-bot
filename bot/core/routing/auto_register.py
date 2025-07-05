from abc import ABC, abstractmethod

from aiogram_dialog import Dialog


class AutoRegister(ABC):
    """Дочерние классы автоматически становятся видны для DialogCollector"""

    @staticmethod
    @abstractmethod
    def get_dialog() -> Dialog:
        raise NotImplementedError
