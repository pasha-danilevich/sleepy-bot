from aiogram import Router
from aiogram_dialog.api.entities import ChatEvent
from aiogram_dialog.api.internal import DialogManagerFactory
from aiogram_dialog.api.protocols import (
    DialogRegistryProtocol,
    MediaIdStorageProtocol,
    MessageManagerProtocol,
)

from bot.core.dialog_manager.custom_dialog_manager import DialogManagerWithDTO


class ManagerFactory(DialogManagerFactory):
    def __init__(
        self,
        message_manager: MessageManagerProtocol,
        media_id_storage: MediaIdStorageProtocol,
    ) -> None:
        self.message_manager = message_manager
        self.media_id_storage = media_id_storage

    def __call__(
        self,
        event: ChatEvent,
        data: dict,
        registry: DialogRegistryProtocol,
        router: Router,
    ) -> DialogManagerWithDTO:
        return DialogManagerWithDTO(
            event=event,
            data=data,
            message_manager=self.message_manager,
            media_id_storage=self.media_id_storage,
            registry=registry,
            router=router,
        )
