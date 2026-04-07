from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class TaskType(Base):
    __tablename__ = "task_type"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    id_skill = Column(Integer, ForeignKey("skill.id"), nullable=False)

    junior_time = Column(Integer, nullable=False)
    middle_time = Column(Integer, nullable=False)
    senior_time = Column(Integer, nullable=False)

    skill = relationship("Skill", back_populates="task_types")
    tasks = relationship("Task", back_populates="task_type")