import datetime
from typing import List

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    password: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_active: bool
    is_staff: bool
    is_superuser: bool


class UserList(BaseModel):
    users: List[UserSchema]
