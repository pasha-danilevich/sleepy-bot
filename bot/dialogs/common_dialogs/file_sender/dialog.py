from io import BytesIO
from typing import Optional

from aiogram.enums import InputMediaType
from aiogram_dialog import Dialog, DialogManager, ShowMode, Window
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Const

from bot.core.routing.auto_register import AutoRegister

from .dto import MediaAttachmentDialogDTO
from .handlers import MediaAttachmentHandler
from .state import MediaAttachmentSG

dialog = Dialog(
    Window(
        Const('Файл готов'),
        Cancel(Const('Закрыть')),
        state=MediaAttachmentSG.start,
    ),
    on_start=MediaAttachmentHandler.on_start,
)


class FileSenderDialog(AutoRegister):
    """Отправляет файл и возвращается к контексту диалога."""

    StateGroup = MediaAttachmentSG

    @staticmethod
    def get_dialog() -> Dialog:
        return dialog

    async def start(
        self,
        manager: DialogManager,
        message_id: int,
        file_name: str,
        buffer: BytesIO,
        caption: Optional[str] = None,
        media_type: InputMediaType = InputMediaType.DOCUMENT,
    ) -> None:
        dto = MediaAttachmentDialogDTO(
            message_id=message_id,
            file_name=file_name,
            buffer=buffer,
            caption=caption,
            media_type=media_type,
        )
        await manager.start(
            self.StateGroup.start,
            data=dto,  # type: ignore
            show_mode=ShowMode.SEND,
        )
