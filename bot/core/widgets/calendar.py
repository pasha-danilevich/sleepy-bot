import locale
from typing import (
    Optional,
    Union,
)

from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.kbd import Calendar
from aiogram_dialog.widgets.kbd.calendar_kbd import CalendarConfig, OnDateSelected
from aiogram_dialog.widgets.widget_event import (
    WidgetEventProcessor,
)


class RussianCalendar(Calendar):
    """При использовании"""

    def __init__(
        self,
        id: str,
        on_click: Union[OnDateSelected, WidgetEventProcessor, None] = None,
        config: Optional[CalendarConfig] = None,
        when: WhenCondition = None,
    ) -> None:
        locale.setlocale(locale.LC_TIME, 'ru')
        super().__init__(id, on_click, config, when)
