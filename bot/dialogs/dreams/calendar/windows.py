from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Cancel
from aiogram_dialog.widgets.text import Const

from . import getters, handlers
from .calendar import CustomCalendar
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
]
