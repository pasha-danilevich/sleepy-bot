import logging

from aiogram_dialog import DialogManager

logger = logging.getLogger(__name__)


async def get_dream_text(dialog_manager: DialogManager, **kwargs: dict) -> dict:
    logger.debug(f"Getting dream text for {dialog_manager.start_data['dream_id']}")  # type: ignore
    return {"dream_text": 'И мне приснилось как я...'}
