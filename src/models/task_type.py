from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship

from src.db.base import Base

task_type_skill = Table(
    "task_type_skill",
    Base.metadata,
    Column("id_task_type", Integer, ForeignKey("task_type.id"), primary_key=True),
    Column("id_skill", Integer, ForeignKey("skill.id"), primary_key=True),
)

class TaskType(Base):
    __tablename__ = "task_type"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(255), nullable=False)

    junior_time = Column(Integer, nullable=False)
    middle_time = Column(Integer, nullable=False)
    senior_time = Column(Integer, nullable=False)

    skills = relationship("Skill", secondary=task_type_skill, back_populates="task_types")
    tasks = relationship("Task", back_populates="task_type")