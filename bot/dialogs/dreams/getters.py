from datetime import date

from aiogram_dialog import DialogManager


async def get_special_dates(dialog_manager: DialogManager, **kwargs):
    special_dates = [date(2025, 7, 1), date(2025, 7, 3)]
    return {
        "special_dates": special_dates,
    }
