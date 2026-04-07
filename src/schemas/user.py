from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    login: str
    name: str
    surname: str
    lastname: Optional[str] = None
    role: str = Field(..., pattern="^(admin|dispatcher|engineer)$")
    is_active: bool = True


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    login: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    lastname: Optional[str] = None
    role: Optional[str] = Field(None, pattern="^(admin|dispatcher|engineer)$")
    is_active: Optional[bool] = None


class User(UserBase):
    id: int
    date_created: datetime

    class Config:
        from_attributes = True