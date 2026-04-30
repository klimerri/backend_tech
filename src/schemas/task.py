from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    id_task_type: int
    name: str
    text: Optional[str] = None
    priority: int
    id_engineer: Optional[int] = None
    id_location: int
    id_request: int


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    id_task_type: Optional[int] = None
    name: Optional[str] = None
    text: Optional[str] = None
    priority: Optional[int] = None
    id_engineer: Optional[int] = None
    status: Optional[str] = None
    completion_time: Optional[datetime] = None
    estimated_completion_time: Optional[datetime] = None
    actual_completion_time: Optional[datetime] = None
    id_location: Optional[int] = None
    id_request: Optional[int] = None


class TaskOut(TaskBase):
    id: int
    status: str
    completion_time: Optional[datetime]
    estimated_completion_time: Optional[datetime]
    actual_completion_time: Optional[datetime]

    class Config:
        orm_mode = True
        from_attributes = True