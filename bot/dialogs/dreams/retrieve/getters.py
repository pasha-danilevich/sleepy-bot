import logging

from aiogram_dialog import DialogManager

logger = logging.getLogger(__name__)


async def get_selected_date(dialog_manager: DialogManager, **kwargs: dict) -> dict:
    return {"selected_date": dialog_manager.start_data['selected_date']}  # type: ignore


async def get_dream_text(dialog_manager: DialogManager, **kwargs: dict) -> dict:
    # имея selected_date можем получить одну запись
    return {"dream_text": 'И мне приснилось как я...'}


async def get_dream_rating(dialog_manager: DialogManager, **kwargs: dict) -> dict:
    # имея selected_date можем получить одну запись
    return {"dream_rating": 4}
