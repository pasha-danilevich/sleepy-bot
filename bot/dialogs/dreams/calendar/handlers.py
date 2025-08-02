import logging
from datetime import date

from aiogram_dialog import ChatEvent, DialogManager
from aiogram_dialog.widgets.kbd import ManagedCalendar
from dishka import FromDishka
from dishka.integrations.aiogram_dialog import inject

from bot.dialogs.dreams.list.state import DreamsListSG
from bot.dialogs.dreams.retrieve.dialog import RetrieveDreamDialog
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

    sleep_records = await service.sleep_record_repo.filter_by_date(
        user_id=user.id, date=selected_date
    )
    if sleep_records:
        if len(sleep_records) == 1:
            logger.debug('Найдена одна запись')
            await RetrieveDreamDialog.start(manager, selected_date)
        else:
            logger.debug('Найдено больше одной записи')
            await manager.start(DreamsListSG.start, data={'selected_date': selected_date})
    else:
        logger.debug('Ни одной записи не найдено')
        await RetrieveDreamDialog.start_no_dream(manager)
