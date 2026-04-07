from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.database import get_db
from src.schemas.client import ClientCreate, ClientUpdate, ClientOut
from src.services import client as client_service

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/", response_model=ClientOut)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    try:
        return client_service.create_client(db, client)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[ClientOut])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return client_service.get_clients(db, skip, limit)


@router.get("/{client_id}", response_model=ClientOut)
def read_client(client_id: int, db: Session = Depends(get_db)):
    client = client_service.get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client


@router.put("/{client_id}", response_model=ClientOut)
def update_client(client_id: int, client: ClientUpdate, db: Session = Depends(get_db)):
    try:
        updated_client = client_service.update_client(db, client_id, client)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not updated_client:
        raise HTTPException(status_code=404, detail="Client not found")

    return updated_client


@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    deleted_client = client_service.delete_client(db, client_id)
    if not deleted_client:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"detail": "Client deleted"}