from sqlalchemy.orm import Session
from src.models.client import Client
from src.schemas.client import ClientCreate, ClientUpdate


def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()


def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Client).offset(skip).limit(limit).all()


def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.model_dump())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def update_client(db: Session, client_id: int, client: ClientUpdate):
    db_client = get_client(db, client_id)
    if not db_client:
        return None

    update_data = client.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_client, key, value)

    db.commit()
    db.refresh(db_client)
    return db_client


def delete_client(db: Session, client_id: int):
    db_client = get_client(db, client_id)
    if not db_client:
        return None

    db.delete(db_client)
    db.commit()
    return db_client