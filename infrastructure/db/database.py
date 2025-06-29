import asyncio
from functools import wraps

from loguru import logger
from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError

from config import Config
from infrastructure.di.app.container import container

_config = asyncio.run(container.get(Config))

TORTOISE_ORM = {
    "connections": {"default": _config.default_bd.get_connection_config()},
    "apps": {
        "models": {
            "models": ['aerich.models', "infrastructure.db.tables"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
}


def tortoise_connect(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            await Tortoise.init(config=TORTOISE_ORM)
            return await func(*args, **kwargs)
        finally:
            await Tortoise.close_connections()

    return wrapper


async def ping_db():
    """
    Проверяет подключение к базе данных через Tortoise ORM
    """
    try:
        conn = Tortoise.get_connection("default")
        await conn.execute_query("SELECT 1")
        logger.success("✅ Успешное подключение к PostgreSQL через Tortoise ORM!")
        return True
    except DBConnectionError as e:
        logger.error(f"❌ Ошибка подключения к базе данных: {e}")
        return False
    except Exception as e:
        logger.error(f"❌ Неожиданная ошибка: {e}")
        return False


async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await ping_db()


async def main():
    await init_db()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
