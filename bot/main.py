import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs
from aiogram_dialog.context.media_storage import MediaIdStorage
from aiogram_dialog.manager.message_manager import MessageManager
from dishka import make_async_container
from dishka.integrations.aiogram import setup_dishka
from loguru import logger

from bot.core.dialog_manager.dialog_manager_factory import ManagerFactory
from bot.dialogs import main_dialog
from bot.handlers import main_router
from bot.middlewares.register import register_middlewares
from config import Config
from infrastructure.db.database import init_db
from infrastructure.di.app import get_all_app_providers


def setup_logging():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler()],
    )
    logging.getLogger("tg_bot").setLevel(logging.DEBUG)


async def main():
    setup_logging()
    await init_db()
    config = Config()

    bot = Bot(token=config.bot.BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.include_router(main_router)
    dp.include_router(main_dialog)

    container = make_async_container(*get_all_app_providers())
    setup_dishka(container=container, router=dp)

    register_middlewares(dp)
    setup_dialogs(
        dp,
        dialog_manager_factory=ManagerFactory(
            message_manager=MessageManager(),
            media_id_storage=MediaIdStorage(),
        ),
    )

    logger.success('Бот запущен!')

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await container.close()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
