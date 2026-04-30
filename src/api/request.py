from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.schemas.request import RequestCreate, RequestUpdate, RequestOut
from src.services import request as service

router = APIRouter(prefix="/requests", tags=["Requests"])


@router.post("/", response_model=RequestOut)
def create(data: RequestCreate, db: Session = Depends(get_db)):
    try:
        return service.create(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[RequestOut])
def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip, limit)


@router.get("/{request_id}", response_model=RequestOut)
def get(request_id: int, db: Session = Depends(get_db)):
    obj = service.get(db, request_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Request not found")
    return obj


@router.put("/{request_id}", response_model=RequestOut)
def update(request_id: int, data: RequestUpdate, db: Session = Depends(get_db)):
    try:
        obj = service.update(db, request_id, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not obj:
        raise HTTPException(status_code=404, detail="Request not found")

    return obj


@router.delete("/{request_id}")
def delete(request_id: int, db: Session = Depends(get_db)):
    obj = service.delete(db, request_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Request not found")
    return {"detail": "Deleted"}


@router.get("/{request_id}/tasks")
def get_tasks_by_request_id(request_id: int, db: Session = Depends(get_db)):
    result = service.get_tasks(db, request_id)
    return result