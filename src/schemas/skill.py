from pydantic import BaseModel
from typing import Optional

class SkillBase(BaseModel):
    name: str


class SkillCreate(SkillBase):
    pass


class SkillUpdate(BaseModel):
    name: Optional[str] = None


class SkillOut(SkillBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True