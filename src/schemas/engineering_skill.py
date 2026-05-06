from pydantic import BaseModel

from src.schemas.skill import SkillOut


class EngineeringSkillBase(BaseModel):
    id_engineer: int
    id_skill: int
    level: int


class EngineeringSkillCreate(EngineeringSkillBase):
    pass


class EngineeringSkillOut(EngineeringSkillBase):
    id: int
    skill: SkillOut

    class Config:
        orm_mode = True
        from_attributes = True