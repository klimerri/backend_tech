from pydantic import BaseModel, Field
from typing import Optional


class EngineerBase(BaseModel):
    id_user: int
    seniority: str = Field(..., pattern="^(junior|middle|senior)$")
    weekly_hours: int
    workload: int
    id_location: int


class EngineerCreate(EngineerBase):
    pass


class EngineerUpdate(BaseModel):
    seniority: Optional[str] = Field(None, pattern="^(junior|middle|senior)$")
    weekly_hours: Optional[int] = None
    workload: Optional[int] = None
    id_location: Optional[int] = None


class EngineerOut(EngineerBase):
    id: int

    class Config:
        from_attributes = True