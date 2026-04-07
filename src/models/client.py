from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base

class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(12), nullable=False)
    mail = Column(String(255), nullable=False)
    telegram = Column(String(255), nullable=True)

    id_location = Column(Integer, ForeignKey("location.id"), nullable=False)

    location = relationship("Location", back_populates="clients")
    requests = relationship("Request", back_populates="client")