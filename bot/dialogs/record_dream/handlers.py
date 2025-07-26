import logging
from datetime import date
from typing import TypedDict

from aiogram_dialog import DialogManager

logger = logging.getLogger(__name__)


class StartData(TypedDict):
    create_date: date


async def on_start(start_data: StartData, manager: DialogManager) -> None:
    logger.debug(f'{start_data=}')
