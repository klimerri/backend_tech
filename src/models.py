from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.orm import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class UserRole(str, enum.Enum):
    admin = "admin"
    engineer = "engineer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(50), unique=True, index=True, nullable=False)
    user_name = Column(String(100), nullable=True)
    user_surname = Column(String(100), nullable=True)
    password = Column(String(255), nullable=False)
    
    is_active = Column(Boolean, default=True)
    role = Column(Enum(UserRole), default=UserRole.engineer)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)