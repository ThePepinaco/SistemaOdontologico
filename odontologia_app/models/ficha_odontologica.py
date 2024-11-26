from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from models.database import Base

class FichaOdontologica(Base):
    __tablename__ = "fichas_odontologicas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    tratamiento_realizado = Column(String, nullable=False)
    costo = Column(Float, nullable=False)
    abono = Column(Float, nullable=True)
    saldo = Column(Float, nullable=True)

    cliente = relationship("Cliente", back_populates="fichas_odontologicas")
