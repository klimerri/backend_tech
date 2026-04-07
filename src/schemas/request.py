from pydantic import BaseModel
from typing import Optional
from datetime import date


class RequestBase(BaseModel):
    id_client: int
    header: str
    text: Optional[str] = None


class RequestCreate(RequestBase):
    pass


class RequestUpdate(BaseModel):
    id_client: Optional[int] = None
    header: Optional[str] = None
    text: Optional[str] = None
    date: Optional[date] = None


class RequestOut(RequestBase):
    id: int
    date: date

    class Config:
        from_attributes = True