from typing import Optional

from infrastructure.db.tables import User

from .dto import UserDTO


class UserRepo:
    @staticmethod
    async def _get_user_by_id(user_id: int) -> Optional[User]:
        """Получение пользователя по ID. Если нет - вызывает DoesNotExist"""
        return await User.get(id=user_id)

    @classmethod
    async def get_user(cls, user_id: int) -> UserDTO:
        """Получение пользователя в виде UserDTO"""
        user = await cls._get_user_by_id(user_id)
        return UserDTO(**await user.to_dict())

    @staticmethod
    async def update_or_create_user(user: UserDTO) -> UserDTO:
        """создание или обновление пользователя возвращает UserDto"""
        user, created = await User.update_or_create(
            defaults=user.model_dump(exclude_none=False, exclude_unset=True),
            id=user.id,
        )
        return UserDTO(**await user.to_dict())

    # установление для пользователя признака не активен
    async def inactive_user(self, user_id: int) -> None:
        user: User = await self._get_user_by_id(user_id)
        user.is_active = False
        await user.save()

    async def get_user_by_id(self, user_id: int) -> UserDTO:
        user = await self._get_user_by_id(user_id)
        return UserDTO(**await user.to_dict())
