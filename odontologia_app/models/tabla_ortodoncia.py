from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.database import Base


class TablaOrtodoncia(Base):
    __tablename__ = "tabla_ortodoncia"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    relacion_molar = Column(Float, nullable=True)
    overejet = Column(Float, nullable=True)
    overbite = Column(Float, nullable=True)
    mandibular_incisivo_extrusion = Column(Float, nullable=True)
    interincisal_angulo = Column(Float, nullable=True)
    u_incisivo_protusion = Column(Float, nullable=True)
    l1_protusion = Column(Float, nullable=True)
    u_incisivo_inclinacio = Column(Float, nullable=True)
    l1_a_po = Column(Float, nullable=True)
    occl_plano_fh = Column(Float, nullable=True)
    u6_pt_vertical = Column(Float, nullable=True)
    convexidad = Column(Float, nullable=True)
    arco_mandibula = Column(Float, nullable=True)
    fma = Column(Float, nullable=True)
    depth_maxilar = Column(Float, nullable=True)
    facial_axis_eje_rickets = Column(Float, nullable=True)
    angulo_profundidad_facial = Column(Float, nullable=True)
    facial_taper_na_gn_go = Column(Float, nullable=True)
    lozalizacion_porion = Column(Float, nullable=True)
    craneal_defleccion = Column(Float, nullable=True)
    rama_posicion = Column(Float, nullable=True)
    lower_face_height = Column(Float, nullable=True)
    lower_lip_plano_e = Column(Float, nullable=True)
    resumen = Column(String, nullable=True)
   

    cliente = relationship("Cliente", back_populates="tabla_ortodoncia")
