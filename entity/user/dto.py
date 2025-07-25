from datetime import date
from typing import Optional

from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: Optional[str]
    fullname: Optional[str]
    birthday: Optional[date]
    age: Optional[int]
    gender: Optional[int]
    phone: Optional[str]
    email: Optional[str]


class CreateUserDTO(BaseModel):
    id: int
    username: str


class UpdateUserDTO(BaseModel):
    username: Optional[str] = None
    fullname: Optional[str] = None
    birthday: Optional[date] = None
    age: Optional[int] = None
    gender: Optional[int] = None
    phone: Optional[str] = None
    email: Optional[str] = None
