from pydantic import BaseModel
from typing import Optional
from datetime import date

from src.schemas.client import ClientOut


class RequestBase(BaseModel):
    header: str
    text: Optional[str] = None


class RequestCreate(RequestBase):
    id_client: int


class RequestUpdate(BaseModel):
    id_client: Optional[int] = None
    header: Optional[str] = None
    text: Optional[str] = None
    date: Optional[date] = None


class RequestOut(BaseModel):
    id: int
    date: date
    header: str
    text: Optional[str] = None
    client: ClientOut
    task_ids: list[int] = []

    class Config:
        orm_mode = True
        from_attributes = True