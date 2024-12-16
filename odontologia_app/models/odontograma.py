from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from models.database import Base

class Odontograma(Base):
    __tablename__ = "odontograma"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    cuadro_id = Column(Integer, nullable=False)
    color = Column(String, nullable=False)

    cliente = relationship("Cliente", back_populates="odontogramas")