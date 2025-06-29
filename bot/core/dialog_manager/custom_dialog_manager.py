from typing import Generic, TypeVar

from aiogram_dialog.manager.manager import ManagerImpl
from pydantic import BaseModel

DataTransferObjectType = TypeVar('DataTransferObjectType', bound=BaseModel)


class DialogManagerWithDTO(ManagerImpl, Generic[DataTransferObjectType]):
    """Позволяет, определить новые атрибуты и методы в DialogManager.
    Это работает благодаря утиной типизации и кастомного ManagerImpl`а, который заменил нативный DialogManager.
    Данный класс мы передаем в нашу кастомную фабрику, чтобы под капотом aiogram-dialog работала именно она, а не нативный DialogManager
    """

    async def set_dialog_dto(self, dto: DataTransferObjectType) -> None:
        self.current_context().dialog_data['dto'] = dto

    @property
    def dto(self) -> DataTransferObjectType:
        try:
            return self.current_context().dialog_data['dto']  # type: ignore
        except KeyError:
            raise ValueError(
                "Невозможно получить DTO, так как он не был инициализирован."
                " Используйте set_dialog_dto для установки DTO"
            )
