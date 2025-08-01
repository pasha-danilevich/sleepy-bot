import logging
from datetime import date

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import ChatEvent, DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button, ManagedCalendar
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from bot.dialogs import record_dream
from bot.dialogs.dreams.list.state import DreamsListSG
from bot.dialogs.dreams.state import DreamsSG
from bot.dialogs.record_dream.dialog import RecordDreamDialog
from entity.tracker.service import TrackerService

logger = logging.getLogger(__name__)


@inject
async def on_date_selected(
    _: ChatEvent,
    __: ManagedCalendar,
    manager: DialogManager,
    selected_date: date,
    service: FromDishka[TrackerService],
) -> None:
    logger.debug('Проверяем, если ли запись со сном в БД')
    user = manager.event.from_user
    if not user:
        raise ValueError("No User")

    manager.dialog_data['selected_date'] = selected_date

    sleep_records = await service.sleep_record_repo.filter_by_date(
        user_id=user.id, date=selected_date
    )
    if sleep_records:
        if len(sleep_records) == 1:
            logger.debug('Найдена одна запись')
            await manager.switch_to(DreamsSG.dream)
        else:
            logger.debug('Найдено больше одной записи')
            await manager.start(DreamsListSG.start, data={'selected_date': selected_date})
    else:
        logger.debug('Ни одной записи не найдено')
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
