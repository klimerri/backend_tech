from sqlalchemy.orm import Session

from src.crud import task_type as crud
from src.schemas.task_type import TaskTypeCreate, TaskTypeUpdate


def create(db: Session, data: TaskTypeCreate):
    return crud.create(db, data)


def get(db: Session, task_type_id: int):
    return crud.get(db, task_type_id)


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return crud.get_all(db, skip, limit)


def update(db: Session, task_type_id: int, data: TaskTypeUpdate):
    return crud.update(db, task_type_id, data)


def delete(db: Session, task_type_id: int):
    return crud.delete(db, task_type_id)