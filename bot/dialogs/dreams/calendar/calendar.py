from typing import Dict

from aiogram_dialog.widgets.kbd import (
    CalendarScope,
)
from aiogram_dialog.widgets.kbd.calendar_kbd import (
    CalendarMonthView,
    CalendarScopeView,
    CalendarYearsView,
)

from bot.core.widgets.calendar import RussianCalendar

from .days_view import MarkSpecialCalendarDaysView


class CustomCalendar(RussianCalendar):
    def _init_views(self) -> Dict[CalendarScope, CalendarScopeView]:
        return {
            CalendarScope.DAYS: MarkSpecialCalendarDaysView(self._item_callback_data),
            CalendarScope.MONTHS: CalendarMonthView(self._item_callback_data),
            CalendarScope.YEARS: CalendarYearsView(self._item_callback_data),
        }
