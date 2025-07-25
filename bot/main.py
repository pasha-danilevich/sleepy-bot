import asyncio
import logging.config

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dishka import make_async_container
from dishka.integrations.aiogram import setup_dishka

from bot.setup_utils import setup_bot_components
from config import Config
from infra.db.database import init_db
from infra.di.app import get_all_app_providers
from infra.di.bot import get_all_bot_providers
from infra.di.entity import get_all_entity_providers
from infra.logger.setup import get_dict_config


async def main():
    logging.config.dictConfig(get_dict_config())

    logger = logging.getLogger(__name__)

    await init_db()
    config = Config()

    bot = Bot(token=config.bot.BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    await setup_bot_components(dp)

    container = make_async_container(
        *get_all_app_providers(),
        *get_all_bot_providers(),
        *get_all_entity_providers(),
    )
    setup_dishka(container=container, router=dp)

    bot_name = await bot.get_my_name()
    logger.info(f'Бот "{bot_name.name}" запущен!')

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await container.close()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
