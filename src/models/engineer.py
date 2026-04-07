from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship

from src.database import Base

class Engineer(Base):
    __tablename__ = "engineer"

    id = Column(Integer, primary_key=True, index=True)

    id_user = Column(Integer, ForeignKey("user.id"), nullable=False, unique=True)
    seniority = Column(String(255), nullable=False)
    weekly_hours = Column(Integer, nullable=False)
    workload = Column(Integer, nullable=False)

    id_location = Column(Integer, ForeignKey("location.id"), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "seniority IN ('junior', 'middle', 'senior')",
            name="chk_seniority"
        ),
    )

    user = relationship("User", back_populates="engineer")
    location = relationship("Location", back_populates="engineers")
    engineering_skills = relationship("EngineeringSkill", back_populates="engineer", cascade="all, delete-orphan")
    engineering_skills = relationship("EngineeringSkill",back_populates="skill",cascade="all, delete-orphan")
    tasks = relationship("Task", back_populates="engineer")
