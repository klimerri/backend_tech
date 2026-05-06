from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.schemas.task import TaskCreate, TaskUpdate, TaskOut, TaskOutWithDetails
from src.services import task as service

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskOutWithDetails)
def create(data: TaskCreate, db: Session = Depends(get_db)):
    try:
        return service.create(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[TaskOutWithDetails])
def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip, limit)


@router.get("/{task_id}", response_model=TaskOutWithDetails)
def get(task_id: int, db: Session = Depends(get_db)):
    obj = service.get(db, task_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Task not found")
    return obj


@router.put("/{task_id}", response_model=TaskOutWithDetails)
def update(task_id: int, data: TaskUpdate, db: Session = Depends(get_db)):
    try:
        obj = service.update(db, task_id, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not obj:
        raise HTTPException(status_code=404, detail="Task not found")

    return obj


@router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    obj = service.delete(db, task_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Deleted"}


@router.post("/{task_id}/assign/{engineer_id}", response_model=TaskOutWithDetails)
def assign(task_id: int, engineer_id: int, db: Session = Depends(get_db)):
    try:
        obj = service.assign_engineer(db, task_id, engineer_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not obj:
        raise HTTPException(status_code=404, detail="Task not found")

    return obj


@router.patch("/{task_id}/status", response_model=TaskOutWithDetails)
def update_status(task_id: int, status: str, db: Session = Depends(get_db)):
    try:
        obj = service.update_status(db, task_id, status)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not obj:
        raise HTTPException(status_code=404, detail="Task not found")

    return obj