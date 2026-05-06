from sqlalchemy.orm import Session
from src.models.task import Task
from src.schemas.task import TaskCreate, TaskUpdate


def get(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Task).offset(skip).limit(limit).all()


def create(db: Session, data: TaskCreate):
    obj = Task(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update(db: Session, task_id: int, data: TaskUpdate):
    obj = get(db, task_id)
    if not obj:
        return None

    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)

    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, task_id: int):
    obj = get(db, task_id)
    if not obj:
        return None

    db.delete(obj)
    db.commit()
    return obj