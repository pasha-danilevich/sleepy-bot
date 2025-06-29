from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update
from aiogram_dialog import DialogManager
from aiogram_dialog.api.exceptions import OutdatedIntent, UnknownIntent


class ErrorMiddleware(BaseMiddleware):
    @staticmethod
    async def _error_response(data: dict, event: Update):
        # Получаем dialog_manager только если он есть в data
        dialog_manager: DialogManager | None = data.get("dialog_manager")
        await event.message.answer("⚠️ Сессия устарела. Начните заново: /start")

        # Сбрасываем стек, если dialog_manager доступен
        if dialog_manager:
            await dialog_manager.reset_stack()

        return None  # Прерываем дальнейшую обработку

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: dict,
    ) -> Any:
        try:
            return await handler(event, data)
        except UnknownIntent as e:
            return await self._error_response(data, event)
        except OutdatedIntent as e:
            return await self._error_response(data, event)
