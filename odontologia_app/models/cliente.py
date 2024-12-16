from sqlalchemy import Column, Float, Integer, String, Boolean
from models.database import Base
from sqlalchemy.orm import relationship


class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=True)
    edad = Column(Integer, nullable=True)
    direccion = Column(String, nullable=True)
    telefono = Column(String, nullable=True)
    cedula = Column(String, nullable=True)
    # Campos médicos
    alergias = Column(String, nullable=True)
    hemorragias = Column(String, nullable=True)
    problemas_cardiacos = Column(String, nullable=True)
    diabetes = Column(String, nullable=True)
    hipertension = Column(String, nullable=True)
    anemia = Column(String, nullable=True)
    alergia_medicamentos = Column(String, nullable=True)
    embarazo = Column(String, nullable=True)
    anestesia_previa = Column(String, nullable=True)
    medicamentos = Column(String, nullable=True)
    saldo_total_od = Column(Float, nullable=True, default=0)
    saldo_total_or = Column(Float, nullable=True, default=0)
    
    fichas_odontologicas = relationship("FichaOdontologica", back_populates="cliente")
    
    informacion_ortodoncia = relationship("InformacionOrtodoncia", back_populates="cliente", uselist=False)
    tabla_ortodoncia = relationship("TablaOrtodoncia", back_populates="cliente", uselist=False)
    ficha_ortodoncia = relationship("FichaOrtodoncia", back_populates="cliente", uselist=False)
    responsable = relationship("Responsable", back_populates="cliente", uselist=False)
    odontogramas = relationship("Odontograma", back_populates="cliente", uselist=False)