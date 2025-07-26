from datetime import date

from aiogram_dialog import DialogManager


async def get_special_dates(dialog_manager: DialogManager, **kwargs: dict) -> dict:
    special_dates = [date(2025, 7, 1), date(2025, 7, 3)]
    return {
        "special_dates": special_dates,
        "is_empty": not bool(len(special_dates)),
    }


async def get_selected_date(dialog_manager: DialogManager, **kwargs: dict) -> dict:
    return {"selected_date": dialog_manager.dialog_data['selected_date']}


async def get_dream_text(dialog_manager: DialogManager, **kwargs: dict) -> dict:
    return {"dream_text": 'И мне приснилось как я...'}


async def get_dream_rating(dialog_manager: DialogManager, **kwargs: dict) -> dict:
    return {"dream_rating": 4}
