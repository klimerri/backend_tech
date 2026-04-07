from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from src.database import Base


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)

    id_task_type = Column(Integer, ForeignKey("task_type.id"), nullable=False)
    name = Column(String(255), nullable=False)
    text = Column(String(255), nullable=True)

    priority = Column(Integer, nullable=False)

    id_engineer = Column(Integer, ForeignKey("engineer.id"), nullable=True)

    status = Column(String(20), nullable=False, default="new")

    completion_time = Column(DateTime, nullable=True)
    estimated_completion_time = Column(DateTime, nullable=True)
    actual_completion_time = Column(DateTime, nullable=True)

    id_location = Column(Integer, ForeignKey("location.id"), nullable=False)
    id_request = Column(Integer, ForeignKey("requests.id"), nullable=False)

    task_type = relationship("TaskType", back_populates="tasks")
    engineer = relationship("Engineer", back_populates="tasks")
    location = relationship("Location", back_populates="tasks")
    request = relationship("Request", back_populates="tasks")