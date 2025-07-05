import logging

from aiogram import Dispatcher
from aiogram_dialog import setup_dialogs
from aiogram_dialog.context.media_storage import MediaIdStorage
from aiogram_dialog.manager.message_manager import MessageManager

from bot.core.dialog_manager.dialog_manager_factory import ManagerFactory
from bot.core.routing.collector import DialogCollector
from bot.handlers.commands import router
from bot.middlewares.register import register_middlewares


def setup_logging():
    logging.basicConfig(
        format="%(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler()],
    )
    logging.getLogger("bot").setLevel(logging.DEBUG)

async def setup_bot_components(dp: Dispatcher) -> None:
    """Настройка всех компонентов бота."""
    # Инициализация диалогов
    dialog_collector = DialogCollector()
    dialogs = dialog_collector.collect('bot')
    # print(dialogs)
    dp.include_routers(router, *dialogs)

    # Настройка менеджера диалогов
    dialog_manager = ManagerFactory(
        message_manager=MessageManager(),
        media_id_storage=MediaIdStorage(),
    )
    setup_dialogs(dp, dialog_manager_factory=dialog_manager)

    # Регистрация middleware
    register_middlewares(dp)