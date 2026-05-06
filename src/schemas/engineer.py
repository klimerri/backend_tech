from pydantic import BaseModel, Field
from typing import Optional

from src.schemas.location import Location
from src.schemas.user import User
from src.schemas.engineering_skill import EngineeringSkillOut
from src.schemas.task import TaskOut


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
    user: User
    location: Location
    engineering_skills: list[EngineeringSkillOut] = []
    tasks: list[TaskOut] = []

    class Config:
        orm_mode = True
        from_attributes = True