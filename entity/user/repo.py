from tortoise.contrib.pydantic import pydantic_model_creator

from infra.db.repo.crud import CRUDMixin
from infra.db.tables import User

from .dto import UserDTO

User_pydantic = pydantic_model_creator(User)


class UserRepo(CRUDMixin[UserDTO]):
    model = User
    pydantic_model = User_pydantic
