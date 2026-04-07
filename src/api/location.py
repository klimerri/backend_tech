from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.schemas.location import Location, LocationCreate, LocationUpdate
from backend.crud import location as crud

router = APIRouter(prefix="/locations", tags=["Locations"])


@router.post("/", response_model=Location)
def create(location: LocationCreate, db: Session = Depends(get_db)):
    return crud.create_location(db, location)


@router.get("/", response_model=list[Location])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_locations(db, skip, limit)


@router.get("/{location_id}", response_model=Location)
def read_one(location_id: int, db: Session = Depends(get_db)):
    db_location = crud.get_location(db, location_id)
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@router.put("/{location_id}", response_model=Location)
def update(location_id: int, location: LocationUpdate, db: Session = Depends(get_db)):
    db_location = crud.update_location(db, location_id, location)
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@router.delete("/{location_id}")
def delete(location_id: int, db: Session = Depends(get_db)):
    db_location = crud.delete_location(db, location_id)
    if not db_location:
        raise HTTPException(status_code=404, detail="Location not found")
    return {"message": "Location deleted"}