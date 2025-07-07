from aiogram.types import BufferedInputFile, InputMediaDocument

from bot.core.dialog_manager.custom_dialog_manager import DialogManagerWithDTO
from bot.core.dialog_manager.handler import TypedHandler

from .dto import MediaAttachmentDialogDTO


class MediaAttachmentHandler(TypedHandler):
    DialogManager = DialogManagerWithDTO[MediaAttachmentDialogDTO]

    @staticmethod
    async def on_start(start_data, manager: DialogManager) -> None:
        await manager.set_dialog_dto(start_data)
        dto = manager.dto
        await manager.event.bot.edit_message_media(
            chat_id=manager.event.from_user.id,
            message_id=dto.message_id,
            media=InputMediaDocument(
                media=BufferedInputFile(dto.buffer.getvalue(), filename=dto.file_name),
                caption=dto.caption,
            ),
        )
