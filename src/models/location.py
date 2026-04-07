from sqlalchemy import Column, Integer, String
from backend.database import Base
from sqlalchemy.orm import relationship

class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    street = Column(String(255), nullable=False)
    house = Column(Integer, nullable=False)

    clients = relationship("Client", back_populates="location")
    engineers = relationship("Engineer", back_populates="location")
    tasks = relationship("Task", back_populates="location")