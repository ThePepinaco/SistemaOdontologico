from models.database import SessionLocal
from models.informacion_ortodoncia import InformacionOrtodoncia

# Implementar en el controlador InformacionOrtodonciaController:
class InformacionOrtodonciaController:
    @staticmethod
    def obtener_por_cliente(cliente_id):
        with SessionLocal() as session:
            return session.query(InformacionOrtodoncia).filter_by(cliente_id=cliente_id).first()

    @staticmethod
    def guardar_o_actualizar(cliente_id, **data):
        
        with SessionLocal() as session:
            informacion = session.query(InformacionOrtodoncia).filter_by(cliente_id=cliente_id).first()
            if not informacion:
                informacion = InformacionOrtodoncia(cliente_id=cliente_id, **data)
                session.add(informacion)
            else:
                for key, value in data.items():
                    setattr(informacion, key, value)
            session.commit()
