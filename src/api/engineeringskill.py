from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.schemas.engineering_skill import EngineeringSkillCreate, EngineeringSkillOut
from src.services import engineering_skill as service

router = APIRouter(prefix="/engineering-skills", tags=["Engineering Skills"])


@router.post("/", response_model=EngineeringSkillOut)
def create(data: EngineeringSkillCreate, db: Session = Depends(get_db)):
    try:
        return service.create(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[EngineeringSkillOut])
def get_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return service.get_all(db, skip, limit)


@router.delete("/{es_id}")
def delete(es_id: int, db: Session = Depends(get_db)):
    obj = service.delete(db, es_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return {"detail": "Deleted"}