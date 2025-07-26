import asyncio
import logging
from functools import wraps
from typing import Any, Awaitable, Callable, TypeVar

from tortoise import Tortoise
from tortoise.exceptions import DBConnectionError

from config import Config
from infra.di.app.container import container

logger = logging.getLogger(__name__)
_config = asyncio.run(container.get(Config))

TORTOISE_ORM = {
    "connections": {"default": _config.default_bd.get_connection_config()},
    "apps": {
        "models": {
            "models": ['aerich.models', "infra.db.tables"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
}


T = TypeVar('T')
P = TypeVar('P')


def tortoise_connect(func: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[T]]:
    @wraps(func)
    async def wrapper(*args: P, **kwargs: Any) -> T:
        try:
            await Tortoise.init(config=TORTOISE_ORM)
            return await func(*args, **kwargs)
        finally:
            await Tortoise.close_connections()

    return wrapper


async def ping_db() -> bool:
    """
    Проверяет подключение к базе данных через Tortoise ORM
    """
    try:
        conn = Tortoise.get_connection("default")
        await conn.execute_query("SELECT 1")
        logger.info("✅ Успешное подключение к PostgreSQL через Tortoise ORM!")
        return True
    except DBConnectionError as e:
        logger.error(f"❌ Ошибка подключения к базе данных: {e}")
        return False
    except Exception as e:
        logger.error(f"❌ Неожиданная ошибка: {e}")
        return False


async def init_db() -> None:
    await Tortoise.init(config=TORTOISE_ORM)
    await ping_db()


async def main() -> None:
    await init_db()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
