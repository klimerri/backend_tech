from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.schemas.task_type import TaskTypeCreate, TaskTypeUpdate, TaskTypeOut
from src.services import task_type as service

router = APIRouter(prefix="/task-types", tags=["Task Types"])


@router.post("/", response_model=TaskTypeOut)
def create(data: TaskTypeCreate, db: Session = Depends(get_db)):
    try:
        return service.create(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[TaskTypeOut])
def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip, limit)


@router.get("/{task_type_id}", response_model=TaskTypeOut)
def get(task_type_id: int, db: Session = Depends(get_db)):
    obj = service.get(db, task_type_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Task type not found")
    return obj


@router.put("/{task_type_id}", response_model=TaskTypeOut)
def update(task_type_id: int, data: TaskTypeUpdate, db: Session = Depends(get_db)):
    try:
        obj = service.update(db, task_type_id, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not obj:
        raise HTTPException(status_code=404, detail="Task type not found")

    return obj


@router.delete("/{task_type_id}")
def delete(task_type_id: int, db: Session = Depends(get_db)):
    obj = service.delete(db, task_type_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Task type not found")
    return {"detail": "Deleted"}