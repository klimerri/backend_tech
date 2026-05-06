from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


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
    start_time: Optional[datetime] = None
    completion_time: Optional[datetime] = None
    estimated_completion_time: Optional[datetime] = None
    actual_completion_time: Optional[datetime] = None
    id_location: Optional[int] = None
    id_request: Optional[int] = None


class TaskOut(TaskBase):
    id: int
    status: str
    created_at: datetime
    start_time: Optional[datetime]
    completion_time: Optional[datetime]
    estimated_completion_time: Optional[datetime]
    actual_completion_time: Optional[datetime]

    class Config:
        orm_mode = True
        from_attributes = True


# Nested schemas for detailed task information
class LocationSimple(BaseModel):
    id: int
    name: str
    city: str
    street: str
    house: int

    class Config:
        orm_mode = True
        from_attributes = True


class SkillSimple(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True


class TaskTypeSimple(BaseModel):
    id: int
    name: str
    skills: list[SkillSimple]
    junior_time: int
    middle_time: int
    senior_time: int

    class Config:
        orm_mode = True
        from_attributes = True


class UserSimple(BaseModel):
    id: int
    login: str
    name: str
    surname: str
    lastname: Optional[str] = None
    role: str

    class Config:
        orm_mode = True
        from_attributes = True


class EngineeringWithUser(BaseModel):
    id: int
    id_user: int
    seniority: str
    weekly_hours: int
    workload: int
    id_location: int
    user: UserSimple

    class Config:
        orm_mode = True
        from_attributes = True


class ClientSimple(BaseModel):
    id: int
    name: str
    phone: str
    mail: str
    telegram: Optional[str] = None
    id_location: int

    class Config:
        orm_mode = True
        from_attributes = True


class RequestSimple(BaseModel):
    id: int
    id_client: int
    header: str
    text: Optional[str] = None
    date: date
    client: ClientSimple

    class Config:
        orm_mode = True
        from_attributes = True


class TaskOutWithDetails(BaseModel):
    id: int
    name: str
    text: Optional[str] = None
    priority: int
    status: str
    created_at: datetime
    start_time: Optional[datetime]
    completion_time: Optional[datetime]
    estimated_completion_time: Optional[datetime]
    actual_completion_time: Optional[datetime]
    
    task_type: TaskTypeSimple
    engineer: Optional[EngineeringWithUser] = None
    location: LocationSimple
    request: RequestSimple

    class Config:
        orm_mode = True
        from_attributes = True