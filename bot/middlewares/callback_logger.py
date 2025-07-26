import logging
from typing import Any, Awaitable, Callable, Dict, cast

import click
from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject, Update
from aiogram_dialog.api.entities import Context

logger = logging.getLogger('bot_event_log')


class CallbackLoggerMiddleware(BaseMiddleware):
    EMPTY_STRING = ''

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
            logger.warning("Логгирование не производиться: нет callback_query")
            return result

        context: Context = data['aiogd_context']
        self._log(context, callback)

        return result

    def _log(self, context: Context, callback: CallbackQuery) -> None:
        data_text = (
            f' dialog_data: {context.dialog_data}'
            if context.dialog_data
            else self.EMPTY_STRING
        )
        start_data_text = (
            f' | start_data: {context.start_data} '
            if context.start_data
            else self.EMPTY_STRING
        )
        msg = click.style('Click on:', fg='cyan')
        logger.debug(msg + ' ' + self.get_button_text(callback))

        if data_text or start_data_text:
            msg = click.style('└──> With "Context":', fg='cyan')
            logger.debug(msg + ' ' + data_text + start_data_text)

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

        raise ValueError('Нет кнопок')


# Подключение middleware в диспетчер
