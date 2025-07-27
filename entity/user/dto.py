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
