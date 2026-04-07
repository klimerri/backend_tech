from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from src.database import Base


class EngineeringSkill(Base):
    __tablename__ = "engineering_skill"

    id = Column(Integer, primary_key=True, index=True)

    id_engineer = Column(Integer, ForeignKey("engineer.id"), nullable=False)
    id_skill = Column(Integer, ForeignKey("skill.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint("id_engineer", "id_skill", name="uq_engineer_skill"),
    )

    engineer = relationship("Engineer", back_populates="engineering_skills")
    skill = relationship("Skill", back_populates="engineering_skills")