import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dishka import make_async_container
from dishka.integrations.aiogram import setup_dishka
from loguru import logger

from bot.setup_utils import setup_logging, setup_bot_components
from config import Config
from infrastructure.di.app import get_all_app_providers
from infrastructure.di.bot import get_all_bot_providers


async def main():
    setup_logging()
    # await init_db()
    config = Config()

    bot = Bot(token=config.bot.BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    await setup_bot_components(dp)

    container = make_async_container(*get_all_app_providers(), *get_all_bot_providers())
    setup_dishka(container=container, router=dp)


    bot_name = await bot.get_my_name()
    logger.success(f'Бот "{bot_name.name}" запущен!')

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await container.close()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
