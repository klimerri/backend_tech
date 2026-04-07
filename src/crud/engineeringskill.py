from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from src.models.engineering_skill import EngineeringSkill
from src.schemas.engineering_skill import EngineeringSkillCreate


def get(db: Session, es_id: int):
    return db.query(EngineeringSkill).filter(EngineeringSkill.id == es_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(EngineeringSkill).offset(skip).limit(limit).all()


def create(db: Session, data: EngineeringSkillCreate):
    db_obj = EngineeringSkill(**data.model_dump())
    db.add(db_obj)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("This engineer already has this skill")

    db.refresh(db_obj)
    return db_obj


def delete(db: Session, es_id: int):
    obj = get(db, es_id)
    if not obj:
        return None

    db.delete(obj)
    db.commit()
    return obj