import logging
from typing import Any, Awaitable, Callable, Dict, cast

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject, Update
from aiogram_dialog.api.entities import Context

logger = logging.getLogger(__name__)


class CallbackLoggerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        result = await handler(event, data)
        event_update: Update = data['event_update']

        callback = event_update.callback_query
        if callback is None:
            return result

        context: Context = data['aiogd_context']

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

        if not isinstance(callback.message, Message):
            raise ValueError(
                'Чтобы получить кнопки, тип callback.message должен быть "Message"'
            )

        message = cast(Message, callback.message)

        if message.reply_markup:
            for row in message.reply_markup.inline_keyboard:
                for button in row:
                    if button.callback_data == pressed_data:
                        text = button.text
                        return text
                    raise ValueError('Неизвестный callback')

        raise ValueError('Нет кнопок')


# Подключение middleware в диспетчер
