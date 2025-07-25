from tortoise.contrib.pydantic import pydantic_model_creator

from infra.db.repo.crud import CRUDMixin
from infra.db.tables import User

from .dto import CreateUserDTO, UpdateUserDTO, UserDTO

User_pydantic = pydantic_model_creator(User)


class UserRepo(CRUDMixin[CreateUserDTO, UserDTO, UpdateUserDTO]):
    model = User
    pydantic_model = User_pydantic
