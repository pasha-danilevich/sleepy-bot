import logging
from datetime import date

from aiogram_dialog import DialogManager
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from bot.dialogs.dreams.state import DreamsSG
from bot.dialogs.record_dream.dialog import RecordDreamDialog

logger = logging.getLogger(__name__)


async def on_date_selected(_, __, manager: DialogManager, selected_date: date):
    manager.dialog_data['selected_date'] = selected_date
    logger.debug('Проверяем, если ли запись со сном в БД')
    dream = None
    if dream is not None:
        await manager.switch_to(DreamsSG.dream)
    else:
        await manager.switch_to(DreamsSG.new_dream)


@inject
async def start_record_dream(
    _, __, manager: DialogManager, dialog: FromDishka[RecordDreamDialog]
):
    data = {'create_date': manager.dialog_data['selected_date']}
    await dialog.start(manager, data)


async def on_input_dream_text(_, __, manager: DialogManager, data: str):
    logger.debug(f'Пишем {data} в БД')
    await manager.next()
