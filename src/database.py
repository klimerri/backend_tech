from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models 

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:3745@localhost:3306/pyt"  # Замените user/password/db_name

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)  # Перенесено после импорта models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()