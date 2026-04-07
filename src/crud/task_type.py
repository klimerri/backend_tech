from sqlalchemy.orm import Session
from src.models.task_type import TaskType
from src.schemas.task_type import TaskTypeCreate, TaskTypeUpdate


def get(db: Session, task_type_id: int):
    return db.query(TaskType).filter(TaskType.id == task_type_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TaskType).offset(skip).limit(limit).all()


def create(db: Session, data: TaskTypeCreate):
    db_obj = TaskType(**data.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update(db: Session, task_type_id: int, data: TaskTypeUpdate):
    obj = get(db, task_type_id)
    if not obj:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)

    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, task_type_id: int):
    obj = get(db, task_type_id)
    if not obj:
        return None

    db.delete(obj)
    db.commit()
    return obj