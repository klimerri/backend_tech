from sqlalchemy.orm import Session
from src.crud import client as client_crud
from src.models.location import Location
from src.schemas.client import ClientCreate, ClientUpdate


def create_client(db: Session, client: ClientCreate):
    location = db.query(Location).filter(Location.id == client.id_location).first()
    if not location:
        raise ValueError("Location not found")

    return client_crud.create_client(db, client)


def get_client(db: Session, client_id: int):
    return client_crud.get_client(db, client_id)


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return client_crud.get_clients(db, skip, limit)


def update_client(db: Session, client_id: int, client: ClientUpdate):
    if client.id_location:
        location = db.query(Location).filter(Location.id == client.id_location).first()
        if not location:
            raise ValueError("Location not found")

    return client_crud.update_client(db, client_id, client)


def delete_client(db: Session, client_id: int):
    return client_crud.delete_client(db, client_id)