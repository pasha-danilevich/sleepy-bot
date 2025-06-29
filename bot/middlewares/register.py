from aiogram import Dispatcher
from tg_bot.middlewares.callback_logger import CallbackLoggerMiddleware
from tg_bot.middlewares.errors_middleware import ErrorMiddleware


def register_middlewares(dp: Dispatcher):
    dp.callback_query.outer_middleware(CallbackLoggerMiddleware())
    dp.callback_query.outer_middleware(ErrorMiddleware())
