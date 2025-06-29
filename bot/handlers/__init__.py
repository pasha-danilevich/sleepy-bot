from aiogram import Router
from settings import settings

from .commands import router as commands_router

main_router = Router()

main_router.include_router(commands_router)

if settings.bot.PHONE_REQUIRED:
    from tg_bot.dialogs.phone_dialog.callback_handlers import phone_router

    main_router.include_router(phone_router)
