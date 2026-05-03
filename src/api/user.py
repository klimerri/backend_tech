from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.user import User, UserCreate, UserUpdate, UserLogin
from src.crud import user as crud

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=User)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("/", response_model=list[User])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)


@router.get("/{user_id}", response_model=User)
def read_one(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=User)
def update(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}


@router.post("/login")
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, user_credentials.login, user_credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"role": user.role, "name": user.name, "lastname": user.surname}