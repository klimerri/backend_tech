from pydantic import BaseModel

class LocationBase(BaseModel):
    name: str
    city: str
    street: str
    house: int


class LocationCreate(LocationBase):
    pass


class LocationUpdate(BaseModel):
    name: str | None = None
    city: str | None = None
    street: str | None = None
    house: int | None = None


class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True