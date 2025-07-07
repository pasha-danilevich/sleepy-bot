from io import BytesIO
from typing import Optional

from aiogram.enums import InputMediaType
from pydantic import BaseModel, ConfigDict


class MediaAttachmentDialogDTO(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)  # Разрешаем произвольные типы
    message_id: int
    file_name: str
    buffer: BytesIO
    caption: Optional[str]
    media_type: InputMediaType = InputMediaType.DOCUMENT
