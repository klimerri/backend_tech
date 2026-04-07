from sqlalchemy import Column, Integer, String, Boolean, DateTime, CheckConstraint
from datetime import datetime
from sqlalchemy.orm import relationship

from src.db.base import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=True)

    role = Column(String(8), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    date_created = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        CheckConstraint(
            "role IN ('admin', 'dispatcher', 'engineer')",
            name="chk_role"
        ),
    )

    engineer = relationship("Engineer", back_populates="user", uselist=False)