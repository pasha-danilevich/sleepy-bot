from aiogram.enums.parse_mode import ParseMode
from aiogram_dialog import Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Cancel, Row, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from ...core.sugar.widgets.buttons import BACK_AND_CANCEL
from . import getters, handlers
from .calendar.calendar import CustomCalendar
from .state import DreamsSG

windows = [
    Window(
        Const("Календарь ваших снов:"),
        Const(
            'Вы пока что не записывали свои сны, когда запишите свой первый сон, он появится'
            ' тут под эмодзи "💤"',
            when='is_empty',
        ),
        CustomCalendar(id='custom_calendar', on_click=handlers.on_date_selected),
        Cancel(Const("Закрыть")),
        state=DreamsSG.start,
        getter=getters.get_special_dates,
    ),
    Window(
        Format("{selected_date}"),
        Const(" "),
        Const("На этот день вы не записывали сон. "),
        Button(
            Const('Записать сновидение'),
            id='record_dream',
            on_click=handlers.start_record_dream,
        ),
        BACK_AND_CANCEL,
        state=DreamsSG.new_dream,
        getter=getters.get_selected_date,
    ),
    Window(
        Format("{selected_date}"),
        Format("Качество сна: {dream_rating}"),
        Const(" "),
        Format('`{dream_text}`'),
        SwitchTo(Const("Изменить"), id='edit', state=DreamsSG.edit),
        Row(
            SwitchTo(Const('Назад'), state=DreamsSG.start, id='back'),
            Cancel(Const("На главную")),
        ),
        state=DreamsSG.dream,
        getter=[getters.get_selected_date, getters.get_dream_text, getters.get_dream_rating],
        parse_mode=ParseMode.MARKDOWN,
    ),
    Window(
        Const("На данный момент, ваш сон звучит так:"),
        Const(" "),
        Format('`{dream_text}`'),
        Const(" "),
        Const("Скопируйте его, измените и отправьте."),
        TextInput(id='text', on_success=handlers.on_input_dream_text),
        BACK_AND_CANCEL,
        state=DreamsSG.edit,
        getter=[getters.get_selected_date, getters.get_dream_text],
        parse_mode=ParseMode.MARKDOWN,
    ),
    Window(
        Const('Отлично. Вы можете найти свой сон в вкладке "Мои сновидения"'),
        Row(
            SwitchTo(Const('В календарь'), state=DreamsSG.start, id='back'),
            Cancel(Const("На главную")),
        ),
        state=DreamsSG.done,
    ),
]
