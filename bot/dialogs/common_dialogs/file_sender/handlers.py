from typing import Any, cast

from aiogram.types import BufferedInputFile, InputMediaDocument, User

from bot.core.dialog_manager.custom_dialog_manager import DialogManagerWithDTO
from bot.core.dialog_manager.handler import TypedHandler

from .dto import MediaAttachmentDialogDTO


class MediaAttachmentHandler(TypedHandler):
    DialogManager = DialogManagerWithDTO[MediaAttachmentDialogDTO]

    @staticmethod
    async def on_start(start_data: Any, manager: DialogManager) -> None:
        await manager.set_dialog_dto(start_data)
        user = cast(User, manager.event.from_user)
        dto = manager.dto
        bot = manager.event.bot

        if not bot:
            raise ValueError('No Bot')

        await bot.edit_message_media(
            chat_id=user.id,
            message_id=dto.message_id,
            media=InputMediaDocument(
                media=BufferedInputFile(dto.buffer.getvalue(), filename=dto.file_name),
                caption=dto.caption,
            ),
        )
