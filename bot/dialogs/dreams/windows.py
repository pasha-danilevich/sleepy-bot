from aiogram_dialog import Window
from aiogram_dialog.widgets.text import Const

from . import getters, handlers
from .calendar.calendar import CustomCalendar
from .state import DreamsSG

windows = [
    Window(
        Const("Календарь ваших снов"),
        CustomCalendar(id='custom_calendar', on_click=handlers.on_date_selected),
        state=DreamsSG.start,
        getter=getters.get_special_dates,
    )
]
