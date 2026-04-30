

from sqlalchemy import select
from sqlalchemy.orm import Session
from src.crud import request as crud
from src.models.client import Client
from src.models.task import Task
from src.schemas.request import RequestCreate, RequestUpdate


def create(db: Session, data: RequestCreate):
    client = db.query(Client).filter(Client.id == data.id_client).first()
    if not client:
        raise ValueError("Client not found")

    return crud.create(db, data)


def get(db: Session, request_id: int):
    return crud.get(db, request_id)


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return crud.get_all(db, skip, limit)


def update(db: Session, request_id: int, data: RequestUpdate):
    if data.id_client:
        client = db.query(Client).filter(Client.id == data.id_client).first()
        if not client:
            raise ValueError("Client not found")

    return crud.update(db, request_id, data)


def delete(db: Session, request_id: int):
    return crud.delete(db, request_id)

def get_tasks(db: Session, request_id: int):
    result = db.execute(select(Task).filter(Task.id_request == request_id))
    tasks = result.scalars().all()

    return tasks