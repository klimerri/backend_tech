from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.schemas.engineer import EngineerCreate, EngineerUpdate, EngineerOut
from src.services import engineer as engineer_service

router = APIRouter(prefix="/engineers", tags=["Engineers"])


@router.post("/", response_model=EngineerOut)
def create_engineer(engineer: EngineerCreate, db: Session = Depends(get_db)):
    try:
        return engineer_service.create_engineer(db, engineer)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[EngineerOut])
def read_engineers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return engineer_service.get_engineers(db, skip, limit)


@router.get("/{engineer_id}", response_model=EngineerOut)
def read_engineer(engineer_id: int, db: Session = Depends(get_db)):
    engineer = engineer_service.get_engineer(db, engineer_id)
    if not engineer:
        raise HTTPException(status_code=404, detail="Engineer not found")
    return engineer


@router.put("/{engineer_id}", response_model=EngineerOut)
def update_engineer(engineer_id: int, engineer: EngineerUpdate, db: Session = Depends(get_db)):
    try:
        updated_engineer = engineer_service.update_engineer(db, engineer_id, engineer)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not updated_engineer:
        raise HTTPException(status_code=404, detail="Engineer not found")

    return updated_engineer


@router.delete("/{engineer_id}")
def delete_engineer(engineer_id: int, db: Session = Depends(get_db)):
    deleted_engineer = engineer_service.delete_engineer(db, engineer_id)
    if not deleted_engineer:
        raise HTTPException(status_code=404, detail="Engineer not found")
    return {"detail": "Engineer deleted"}