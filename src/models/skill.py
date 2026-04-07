from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base


class Skill(Base):
    __tablename__ = "skill"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    task_types = relationship("TaskType", back_populates="skill")