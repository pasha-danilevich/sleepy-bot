from aiogram import Dispatcher
from .callback_logger import CallbackLoggerMiddleware
from .errors_middleware import ErrorMiddleware


def register_middlewares(dp: Dispatcher):
    dp.callback_query.outer_middleware(CallbackLoggerMiddleware())
    dp.callback_query.outer_middleware(ErrorMiddleware())
