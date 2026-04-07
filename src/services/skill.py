from sqlalchemy.orm import Session
from src.crud import skill as skill_crud
from src.schemas.skill import SkillCreate, SkillUpdate


def create_skill(db: Session, skill: SkillCreate):
    return skill_crud.create_skill(db, skill)


def get_skill(db: Session, skill_id: int):
    return skill_crud.get_skill(db, skill_id)


def get_skills(db: Session, skip: int = 0, limit: int = 100):
    return skill_crud.get_skills(db, skip, limit)


def update_skill(db: Session, skill_id: int, skill: SkillUpdate):
    return skill_crud.update_skill(db, skill_id, skill)


def delete_skill(db: Session, skill_id: int):
    return skill_crud.delete_skill(db, skill_id)