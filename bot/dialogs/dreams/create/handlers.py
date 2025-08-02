import logging
from datetime import date
from typing import TypedDict

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput

logger = logging.getLogger(__name__)


class StartData(TypedDict):
    create_date: date


async def on_start(start_data: StartData, manager: DialogManager) -> None:
    logger.debug(f'{start_data=}')


async def input_dream_text(
    _: Message, __: ManagedTextInput, manager: DialogManager, text: str
) -> None:
    logger.debug(f'{text=}')
