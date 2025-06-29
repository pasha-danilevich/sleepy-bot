from abc import ABC, abstractmethod
from typing import Type

from .custom_dialog_manager import DataTransferObjectType, DialogManagerWithDTO


class TypedHandler(ABC):
    """Унаследовать, если хотим отделить NameSpace для кастомного типа DialogManager"""

    @property
    @abstractmethod
    def DialogManager(self) -> Type[DialogManagerWithDTO[DataTransferObjectType]]:
        """Должен возвращать конкретизированный DialogManager[ConcreteDTO]"""
        raise NotImplementedError("Must define DialogManager with concrete generic types")
