from aiogram import Router

from .home.dialog import dialog as home_dialog

main_dialog = Router()

main_dialog.include_router(home_dialog)
