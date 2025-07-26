from typing import Any, Awaitable, Callable, Dict, cast

from aiogram import BaseMiddleware, types
from aiogram.types import ErrorEvent, TelegramObject, Update
from aiogram_dialog import DialogManager


async def on_unknown_intent(event: ErrorEvent, dialog_manager: DialogManager) -> None:
    # Получаем бота из менеджера диалогов
    bot = dialog_manager.middleware_data["bot"]
    callback = event.update.callback_query
    if not callback:
        raise ValueError('Нет callback_query')

    user = cast(types.user.User, callback.from_user)

    if not callback.message:
        raise ValueError('Нет message')

    message_id = callback.message.message_id

    try:
        # Редактируем сообщение
        await bot.edit_message_text(
            chat_id=user.id,
            message_id=message_id,
            text="⚠️ Сессия устарела. Пожалуйста, начните заново: /start",
            reply_markup=None,  # Убираем клавиатуру
        )
    except Exception as e:
        print(f"Ошибка при редактировании сообщения: {e}")
        # Если не получилось изменить, отправляем новое сообщение
        await bot.send_message(
            chat_id=user.id, text="⚠️ Сессия устарела. Пожалуйста, начните заново: /start"
        )


class UnknownErrorMiddleware(BaseMiddleware):
    @staticmethod
    async def _error_response(data: dict, event: TelegramObject) -> None:
        event = cast(Update, event)
        bot = data.get("bot")
        chat_id = None
        message_id = None

        # Получаем message из разных типов событий
        if event.message:
            chat_id = event.message.chat.id
            message_id = event.message.message_id
        elif event.callback_query and event.callback_query.message:
            chat_id = event.callback_query.message.chat.id
            message_id = event.callback_query.message.message_id

        if bot and chat_id and message_id:
            try:
                await bot.edit_message_text(
                    chat_id=chat_id,
                    message_id=message_id,
                    text="⚠️ Что-то пошло не так. Начните заново: /start",
                    parse_mode="HTML",
                )
            except Exception as edit_error:
                # Если не удалось изменить сообщение, отправляем новое
                await bot.send_message(
                    chat_id=chat_id, text="⚠️ Что-то пошло не так. Начните заново: /start"
                )
        else:
            # Если нет данных для редактирования, отправляем новое сообщение
            if event.message:
                await event.message.answer("⚠️ Что-то пошло не так. Начните заново: /start")

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict,
    ) -> Any:
        try:
            return await handler(event, data)
        except Exception as e:
            return await self._error_response(data, event)
