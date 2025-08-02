import datetime
import logging

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.dialogs import dreams

logger = logging.getLogger(__name__)


async def start_edit_dialog(_: CallbackQuery, __: Button, manager: DialogManager) -> None:
    # имея selected_date можем получить одну запись
    # из нее получаем id
    dream_id = 20
    await dreams.edit.EditDreamDialog().start(manager, dream_id)


async def start_create_dream(_: CallbackQuery, __: Button, manager: DialogManager) -> None:
    # имея selected_date можем получить одну запись передаем ее
    data = dreams.create.StartData(create_date=datetime.date.today())

    await dreams.create.CreateDreamDialog().start(manager, data)
