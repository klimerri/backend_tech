from sqlalchemy.orm import Session

from src.crud import engineering_skill as crud
from src.models.engineer import Engineer
from src.models.skill import Skill
from src.schemas.engineering_skill import EngineeringSkillCreate


def create(db: Session, data: EngineeringSkillCreate):
    engineer = db.query(Engineer).filter(Engineer.id == data.id_engineer).first()
    if not engineer:
        raise ValueError("Engineer not found")

    skill = db.query(Skill).filter(Skill.id == data.id_skill).first()
    if not skill:
        raise ValueError("Skill not found")

    return crud.create(db, data)


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return crud.get_all(db, skip, limit)


def delete(db: Session, es_id: int):
    return crud.delete(db, es_id)