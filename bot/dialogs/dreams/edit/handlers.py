import logging

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

logger = logging.getLogger(__name__)


async def on_input_dream_text(
    _: Message, __: ManagedTextInput, manager: DialogManager, data: str
) -> None:
    logger.debug(f'Пишем {data} в БД')
    await manager.next()
