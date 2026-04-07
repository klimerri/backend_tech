from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class ClientBase(BaseModel):
    name: str
    phone: str = Field(..., max_length=12)
    mail: EmailStr
    telegram: Optional[str] = None
    id_location: int


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = Field(None, max_length=12)
    mail: Optional[EmailStr] = None
    telegram: Optional[str] = None
    id_location: Optional[int] = None


class ClientOut(ClientBase):
    id: int

    class Config:
        from_attributes = True