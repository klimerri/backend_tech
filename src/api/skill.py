from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.schemas.skill import SkillCreate, SkillUpdate, SkillOut
from src.services import skill as skill_service

router = APIRouter(prefix="/skills", tags=["Skills"])


@router.post("/", response_model=SkillOut)
def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    return skill_service.create_skill(db, skill)


@router.get("/", response_model=List[SkillOut])
def read_skills(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return skill_service.get_skills(db, skip, limit)


@router.get("/{skill_id}", response_model=SkillOut)
def read_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = skill_service.get_skill(db, skill_id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill


@router.put("/{skill_id}", response_model=SkillOut)
def update_skill(skill_id: int, skill: SkillUpdate, db: Session = Depends(get_db)):
    updated_skill = skill_service.update_skill(db, skill_id, skill)
    if not updated_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return updated_skill


@router.delete("/{skill_id}")
def delete_skill(skill_id: int, db: Session = Depends(get_db)):
    deleted_skill = skill_service.delete_skill(db, skill_id)
    if not deleted_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return {"detail": "Skill deleted"}