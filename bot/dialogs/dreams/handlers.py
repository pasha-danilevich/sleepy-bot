import logging
from datetime import date

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import ChatEvent, DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button, ManagedCalendar
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from bot.dialogs import record_dream
from bot.dialogs.dreams.state import DreamsSG
from bot.dialogs.record_dream.dialog import RecordDreamDialog

logger = logging.getLogger(__name__)


async def on_date_selected(
    _: ChatEvent, __: ManagedCalendar, manager: DialogManager, selected_date: date
) -> None:
    manager.dialog_data['selected_date'] = selected_date
    logger.debug('Проверяем, если ли запись со сном в БД')
    dream = None
    if dream is not None:
        await manager.switch_to(DreamsSG.dream)
    else:
        await manager.switch_to(DreamsSG.new_dream)


@inject
async def start_record_dream(
    _: CallbackQuery, __: Button, manager: DialogManager, dialog: FromDishka[RecordDreamDialog]
) -> None:
    data = record_dream.StartData(create_date=manager.dialog_data['selected_date'])
    await dialog.start(manager, data)


async def on_input_dream_text(
    _: Message, __: ManagedTextInput, manager: DialogManager, data: str
) -> None:
    logger.debug(f'Пишем {data} в БД')
    await manager.next()
