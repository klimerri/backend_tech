from pydantic import BaseModel
from src.schemas.skill import SkillOut
from src.schemas.skill import SkillOut

class TaskTypeBase(BaseModel):
    name: str
    skills: list[SkillOut]
    junior_time: int
    middle_time: int
    senior_time: int


class TaskTypeCreate(TaskTypeBase):
    pass


class TaskTypeUpdate(BaseModel):
    name: str | None = None
    skills: list[SkillOut] | None = None
    junior_time: int | None = None
    middle_time: int | None = None
    senior_time: int | None = None


class TaskTypeOut(TaskTypeBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True