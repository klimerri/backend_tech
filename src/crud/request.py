from sqlalchemy.orm import Session, joinedload
from src.models.request import Request
from src.schemas.request import RequestCreate, RequestUpdate


def get(db: Session, request_id: int):
    return db.query(Request).options(joinedload(Request.client), joinedload(Request.tasks)).filter(Request.id == request_id).first()


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Request).options(joinedload(Request.client), joinedload(Request.tasks)).offset(skip).limit(limit).all()


def create(db: Session, data: RequestCreate):
    db_obj = Request(**data.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def update(db: Session, request_id: int, data: RequestUpdate):
    obj = get(db, request_id)
    if not obj:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)

    db.commit()
    db.refresh(obj)
    return obj


def delete(db: Session, request_id: int):
    obj = get(db, request_id)
    if not obj:
        return None

    db.delete(obj)
    db.commit()
    return obj