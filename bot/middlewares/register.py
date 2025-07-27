from aiogram import Dispatcher
from aiogram.filters import ExceptionTypeFilter
from aiogram_dialog.api.exceptions import OutdatedIntent, UnknownIntent

from .errors_middleware import UnknownErrorMiddleware, on_unknown_intent
from .logger import CallbackLoggerMiddleware, MessageLoggerMiddleware


def register_middlewares(dp: Dispatcher) -> None:
    dp.callback_query.middleware(UnknownErrorMiddleware())
    dp.callback_query.middleware(CallbackLoggerMiddleware())

    dp.message.middleware(UnknownErrorMiddleware())
    dp.message.middleware(MessageLoggerMiddleware())

    dp.errors.register(
        on_unknown_intent,
        ExceptionTypeFilter(UnknownIntent, OutdatedIntent),
    )
