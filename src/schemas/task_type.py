from pydantic import BaseModel


class TaskTypeBase(BaseModel):
    name: str
    id_skill: int
    junior_time: int
    middle_time: int
    senior_time: int


class TaskTypeCreate(TaskTypeBase):
    pass


class TaskTypeUpdate(BaseModel):
    name: str | None = None
    id_skill: int | None = None
    junior_time: int | None = None
    middle_time: int | None = None
    senior_time: int | None = None


class TaskTypeOut(TaskTypeBase):
    id: int

    class Config:
        from_attributes = True