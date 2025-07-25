import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery
from aiogram_dialog.api.entities import Context

logger = logging.getLogger(__name__)


class CallbackLoggerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any],
    ) -> Any:
        result = await handler(event, data)

        context: Context = data['aiogd_context']
        callback = data.get('event_update').callback_query

        data_text = f' | data: {context.dialog_data} ' if context.dialog_data else ''
        start_data_text = f' | start_data: {context.start_data} ' if context.start_data else ''

        logger.debug(
            f'Click on: "{self.get_button_text(callback)}"{data_text}{start_data_text}'
        )

        return result

    @staticmethod
    def get_button_text(callback: CallbackQuery) -> str:
        """Если нужно получить текст именно той кнопки, которая была нажата"""

        pressed_data = callback.data
        text = None
        for row in callback.message.reply_markup.inline_keyboard:
            for button in row:
                if button.callback_data == pressed_data:
                    text = button.text
                    break
            if text:
                break
        return text


# Подключение middleware в диспетчер
