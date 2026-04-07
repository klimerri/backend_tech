from pydantic import BaseModel


class EngineeringSkillBase(BaseModel):
    id_engineer: int
    id_skill: int


class EngineeringSkillCreate(EngineeringSkillBase):
    pass


class EngineeringSkillOut(EngineeringSkillBase):
    id: int

    class Config:
        from_attributes = True