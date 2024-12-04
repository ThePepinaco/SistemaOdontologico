from sqlalchemy import Column, Float, Integer, String, Boolean, ForeignKey
from models.database import Base
from sqlalchemy.orm import relationship


class Responsable(Base):
    
    __tablename__ = "responsable"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    nombre = Column(String, nullable=True)
    edad = Column(Integer, nullable=True)
    direccion = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    cedula = Column(String, nullable=True)
    correo = Column(String, nullable=True)
    
    cliente = relationship("Cliente", back_populates="responsable")
