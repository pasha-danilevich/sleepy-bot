from typing import Any, Awaitable, Callable, Dict, cast

from aiogram import BaseMiddleware, Bot, types
from aiogram.types import ErrorEvent, Message, TelegramObject, Update
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
    async def _get_message_info(event: TelegramObject) -> tuple[int, int]:
        # Получаем message из разных типов событий
        if isinstance(event, Message):
            message = cast(Message, event)
            if message:
                chat_id = message.chat.id
                message_id = message.message_id
                return chat_id, message_id

        elif isinstance(event, Update):
            event = cast(Update, event)
            if event.message:
                chat_id = event.message.chat.id
                message_id = event.message.message_id
                return chat_id, message_id

        raise ValueError('Unknown event')

    @staticmethod
    async def send_error_msg_to_user(bot: Bot, chat_id: int, message_id: int) -> None:
        try:
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="⚠️ Что-то пошло не так. Начните заново: /start",
                parse_mode="HTML",
            )
        except Exception:
            # Если не удалось изменить сообщение, отправляем новое
            await bot.send_message(
                chat_id=chat_id, text="⚠️ Что-то пошло не так. Начните заново: /start"
            )

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict,
    ) -> Any:
        try:
            return await handler(event, data)
        except Exception:
            bot = data["bot"]

            chat_id, message_id = await self._get_message_info(event)
            await self.send_error_msg_to_user(bot, chat_id, message_id)
            raise  # в добавок выводим ошибку в консоль
