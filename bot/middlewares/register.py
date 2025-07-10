from aiogram import Dispatcher
from aiogram.filters import ExceptionTypeFilter
from aiogram_dialog.api.exceptions import OutdatedIntent, UnknownIntent

from .callback_logger import CallbackLoggerMiddleware
from .errors_middleware import UnknownErrorMiddleware, on_unknown_intent


def register_middlewares(dp: Dispatcher):
    dp.callback_query.middleware(UnknownErrorMiddleware())
    dp.callback_query.outer_middleware(CallbackLoggerMiddleware())

    dp.errors.register(
        on_unknown_intent,
        ExceptionTypeFilter(UnknownIntent, OutdatedIntent),
    )
