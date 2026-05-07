from sqlalchemy.orm import Session
from datetime import datetime

from src.crud import task as crud
from src.models.engineer import Engineer
from src.models.task_type import TaskType
from src.schemas.task import TaskCreate, TaskUpdate
from src.services.planning import plan_new_tasks


VALID_STATUSES = {"new", "process", "done", "cancelled"}
VALID_PRIORITY = {1, 2, 3}


def create(db: Session, data: TaskCreate):
    if data.priority not in VALID_PRIORITY:
        raise ValueError("Invalid priority")

    # проверка task_type
    task_type = db.query(TaskType).filter(TaskType.id == data.id_task_type).first()
    if not task_type:
        raise ValueError("TaskType not found")

    obj = crud.create(db, data)
    return obj


def get(db: Session, task_id: int):
    return crud.get(db, task_id)


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return crud.get_all(db, skip, limit)


def assign_engineer(db: Session, task_id: int, engineer_id: int):
    task = crud.get(db, task_id)
    if not task:
        return None

    engineer = db.query(Engineer).filter(Engineer.id == engineer_id).first()
    if not engineer:
        raise ValueError("Engineer not found")

    task.id_engineer = engineer_id
    task.status = "process"

    db.commit()
    db.refresh(task)
    return task


def update_status(db: Session, task_id: int, status: str):
    if status not in VALID_STATUSES:
        raise ValueError("Invalid status")

    task = crud.get(db, task_id)
    if not task:
        return None

    # Если отмена или завершение, уменьшаем workload инженера на длительность задачи
    if status in ("done", "cancelled") and task.id_engineer:
        engineer = db.query(Engineer).filter(Engineer.id == task.id_engineer).first()
        task_type = db.query(TaskType).filter(TaskType.id == task.id_task_type).first()
       
        if engineer and task_type:
            seniority = engineer.seniority
            if seniority == "junior":
                duration = task_type.junior_time
            elif seniority == "middle":
                duration = task_type.middle_time
            elif seniority == "senior":
                duration = task_type.senior_time
            else:
                duration = 0
            
            # workload не может быть отрицательным
            engineer.workload = max(engineer.workload - duration, 0)
            db.add(engineer)

    task.status = status

    if status == "done":
        task.actual_completion_time = datetime.utcnow()

    db.commit()
    db.refresh(task)
    return task

def cancel_task(db: Session, task_id: int):
    """Отмена заявки с уменьшением workload инженера"""
    return update_status(db, task_id, "cancelled")

def complete_task(db: Session, task_id: int):
    """Завершение заявки с уменьшением workload инженера"""
    return update_status(db, task_id, "done")


def update(db: Session, task_id: int, data: TaskUpdate):
    if data.status and data.status not in VALID_STATUSES:
        raise ValueError("Invalid status")

    return crud.update(db, task_id, data)


def delete(db: Session, task_id: int):
    return crud.delete(db, task_id)