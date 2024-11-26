from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from models.database import Base


class FichaOrtodoncia(Base):
    __tablename__ = "ficha_ortodoncia"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    fecha = Column(Date, nullable=True)
    actividad = Column(String, nullable=True)
    brack = Column(String, nullable=True)
    costo = Column(Float, nullable=True)
    abono = Column(Float, nullable=True)
    saldo = Column(Float, nullable=True)
    

    cliente = relationship("Cliente", back_populates="ficha_ortodoncia")
