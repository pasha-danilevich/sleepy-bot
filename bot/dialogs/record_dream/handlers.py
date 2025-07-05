from datetime import date
from typing import TypedDict

from aiogram_dialog import DialogManager

class StartData(TypedDict):
    create_date: date


async def on_start(start_data: StartData, manager: DialogManager) -> None:
    print(start_data)
