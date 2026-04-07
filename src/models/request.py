from sqlalchemy import Column, Integer, String, Date, ForeignKey, func
from sqlalchemy.orm import relationship

from src.database import Base


class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)

    id_client = Column(Integer, ForeignKey("client.id"), nullable=False)

    header = Column(String(255), nullable=False)
    text = Column(String(255), nullable=True)

    date = Column(Date, nullable=False, server_default=func.current_date())

    client = relationship("Client", back_populates="requests")
    tasks = relationship("Task", back_populates="request")