from sqlalchemy.orm import Session
from src.models.engineer import Engineer
from src.schemas.engineer import EngineerCreate, EngineerUpdate


def get_engineer(db: Session, engineer_id: int):
    return db.query(Engineer).filter(Engineer.id == engineer_id).first()


def get_engineer_by_user_id(db: Session, user_id: int):
    return db.query(Engineer).filter(Engineer.id_user == user_id).first()


def get_engineers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Engineer).offset(skip).limit(limit).all()


def create_engineer(db: Session, engineer: EngineerCreate):
    db_engineer = Engineer(**engineer.model_dump())
    db.add(db_engineer)
    db.commit()
    db.refresh(db_engineer)
    return db_engineer


def update_engineer(db: Session, engineer_id: int, engineer: EngineerUpdate):
    db_engineer = get_engineer(db, engineer_id)
    if not db_engineer:
        return None

    update_data = engineer.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_engineer, key, value)

    db.commit()
    db.refresh(db_engineer)
    return db_engineer


def delete_engineer(db: Session, engineer_id: int):
    db_engineer = get_engineer(db, engineer_id)
    if not db_engineer:
        return None

    db.delete(db_engineer)
    db.commit()
    return db_engineer