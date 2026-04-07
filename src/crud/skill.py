from sqlalchemy.orm import Session
from src.models.skill import Skill
from src.schemas.skill import SkillCreate, SkillUpdate


def get_skill(db: Session, skill_id: int):
    return db.query(Skill).filter(Skill.id == skill_id).first()


def get_skills(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Skill).offset(skip).limit(limit).all()


def create_skill(db: Session, skill: SkillCreate):
    db_skill = Skill(**skill.model_dump())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill


def update_skill(db: Session, skill_id: int, skill: SkillUpdate):
    db_skill = get_skill(db, skill_id)
    if not db_skill:
        return None

    update_data = skill.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_skill, key, value)

    db.commit()
    db.refresh(db_skill)
    return db_skill


def delete_skill(db: Session, skill_id: int):
    db_skill = get_skill(db, skill_id)
    if not db_skill:
        return None

    db.delete(db_skill)
    db.commit()
    return db_skill