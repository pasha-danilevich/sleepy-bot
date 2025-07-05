from typing import Dict

from aiogram_dialog.widgets.kbd import (
    Calendar,
    CalendarScope,
)
from aiogram_dialog.widgets.kbd.calendar_kbd import (
    CalendarMonthView,
    CalendarScopeView,
    CalendarYearsView,
)

from .days_view import CustomCalendarDaysView


class CustomCalendar(Calendar):
    def _init_views(self) -> Dict[CalendarScope, CalendarScopeView]:
        return {
            CalendarScope.DAYS: CustomCalendarDaysView(self._item_callback_data),
            CalendarScope.MONTHS: CalendarMonthView(self._item_callback_data),
            CalendarScope.YEARS: CalendarYearsView(self._item_callback_data),
        }
