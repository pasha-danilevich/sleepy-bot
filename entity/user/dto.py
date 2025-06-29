from datetime import date
from typing import Optional

from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: Optional[str] = None
    fullname: Optional[str] = None
    birthday: Optional[date] = None
    age: Optional[int] = None
    gender: Optional[int] = None
    phone: Optional[str] = None
    email: Optional[str] = None
