from datetime import date

from aiogram.types import InlineKeyboardButton
from aiogram_dialog.api.protocols import DialogManager
from aiogram_dialog.widgets.kbd.calendar_kbd import CalendarDaysView, raw_from_date
from aiogram_dialog.widgets.text import Format


class MarkSpecialCalendarDaysView(CalendarDaysView):
    SPECIAL_DAYS_TEXT = Format("💤 {date:%d}")

    async def _render_date_button(
        self,
        selected_date: date,
        today: date,
        data: dict,
        manager: DialogManager,
    ) -> InlineKeyboardButton:
        current_data = {
            "date": selected_date,
            "data": data,
        }

        special_dates = data.get("special_dates", [])

        if selected_date == today:
            text = self.today_text
        elif selected_date in special_dates:  # Проверяем, есть ли дата в списке
            text = self.SPECIAL_DAYS_TEXT
        else:
            text = self.date_text

        raw_date = raw_from_date(selected_date)

        return InlineKeyboardButton(
            text=await text.render_text(
                current_data,
                manager,
            ),
            callback_data=self.callback_generator(str(raw_date)),
        )
