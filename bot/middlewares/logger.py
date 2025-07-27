import logging
from typing import Any, Awaitable, Callable, Dict, Optional, cast

import click
from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject, Update
from aiogram_dialog.api.entities import Context

event_logger = logging.getLogger('bot_event_log')
context_logger = logging.getLogger('bot_context_log')


class ContextLogger:
    EMPTY_STRING = ''

    def log_context(self, context: Context) -> None:
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

        if data_text or start_data_text:
            msg = click.style('└──> With "Context":', fg='cyan')
            context_logger.debug(msg + ' ' + data_text + start_data_text)


class CallbackLoggerMiddleware(BaseMiddleware, ContextLogger):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        event_update: Update = data['event_update']

        callback = event_update.callback_query
        if callback is None:
            event_logger.warning("Логгирование не производиться: нет callback_query")
            return await handler(event, data)

        msg = click.style('Click on:', fg='cyan')
        event_logger.debug(msg + ' ' + self.get_button_text(callback))

        context: Optional[Context] = data['aiogd_context']
        if context:
            self.log_context(context)

        return await handler(event, data)

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


class MessageLoggerMiddleware(BaseMiddleware, ContextLogger):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        event_update: Update = data['event_update']
        message = event_update.message
        if message is None:
            raise ValueError('Нет объекта "Message"')
        msg = click.style('Send message: ', fg='cyan')
        msg_t = message.text
        event_logger.debug(msg + msg_t if msg_t else '')

        context: Optional[Context] = data['aiogd_context']
        if context:
            self.log_context(context)

        return await handler(event, data)
