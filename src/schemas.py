from pydantic import BaseModel
from typing import Optional
from models import UserRole  

class UserLogin(BaseModel):
    login: str
    password: str 

class UserPublic(BaseModel):
    id: int
    login: str
    role: UserRole
    is_active: bool

    class Config:
        from_attributes = True
