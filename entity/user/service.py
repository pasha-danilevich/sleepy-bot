from .dto import UserDTO
from .repo import UserRepo


class UserService:
    def __init__(
        self,
        user_repo: UserRepo,
    ):
        self.user_repo = user_repo

    async def update_or_create_user(self, user: UserDTO) -> UserDTO:
        return await self.user_repo.update_or_create_user(user)

    async def get_user(self, user_id: int) -> UserDTO:
        return await self.user_repo.get_user_by_id(user_id=user_id)
