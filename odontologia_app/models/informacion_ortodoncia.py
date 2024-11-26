from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base


class InformacionOrtodoncia(Base):
    __tablename__ = "informacion_ortodoncia"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    habitos = Column(String, nullable=True)
    medicamentos = Column(String, nullable=True)
    respiracion = Column(String, nullable=True)
    frenillo_labial = Column(String, nullable=True)
    tercio_aumentado = Column(String, nullable=True)
    cierre_labial = Column(String, nullable=True)
    posicion_lengua = Column(String, nullable=True)
    #Estudios modelos (em)
    em_compresion = Column(String, nullable=True)
    em_expansion = Column(String, nullable=True)
    em_normal = Column(String, nullable=True)
    #Sentigo sagital (ss) maxilar superior (ms) maxilar inferior(mi)
    #Prostusion-retrusion (pr)
    ss_ms_pr_incisivo = Column(String, nullable=True)
    ss_mi_pr_incisivo = Column(String, nullable=True)
    
    
    migragacion = Column(String, nullable=True)
    piezas_auesentes_extraccion = Column(String, nullable=True)
    no_erupcion = Column(String, nullable=True)
    
    #Sentigo vertical (sv) maxilar superior (ms) maxilar inferior(mi)
    sv_ms_piezas_intruidas = Column(String, nullable=True)
    sv_ms_piezas_extruidas = Column(String, nullable=True)
    sv_ms_piezas_sumergidas = Column(String, nullable=True)
    sv_mi_piezas_intruidas = Column(String, nullable=True)
    sv_mi_piezas_extruidas = Column(String, nullable=True)
    sv_mi_piezas_sumergidas = Column(String, nullable=True)
    
    
    terceros_molares_superior = Column(String, nullable=True)
    terceros_molares_inferior = Column(String, nullable=True)
    
    oclusion_mordida_abierta = Column(String, nullable=True)
    oclusion_mordida_profunda = Column(String, nullable=True)
    oclusion_mordida_normal = Column(String, nullable=True)
    
    resalte_overejet = Column(String, nullable=True)
    overvite_escalon = Column(String, nullable=True)
    linea_media_central = Column(String, nullable=True)
    laterales_derecha_rm = Column(String, nullable=True)
    laterales_derecha_rc = Column(String, nullable=True)
    laterales_derecha_cruzada = Column(String, nullable=True)
    laterales_derecha_vis_a_vis = Column(String, nullable=True)
    laterales_izquierda_rm = Column(String, nullable=True)
    laterales_izquierda_rc = Column(String, nullable=True)
    laterales_izquierda_cruzada = Column(String, nullable=True)
    laterales_izquierda_vis_a_vis = Column(String, nullable=True)

    cliente = relationship("Cliente", back_populates="informacion_ortodoncia")
