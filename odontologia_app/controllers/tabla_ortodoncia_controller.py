from models.database import SessionLocal
from models.tabla_ortodoncia import TablaOrtodoncia


class TablaOrtodonciaController:
    @staticmethod
    def obtener_por_cliente(cliente_id):
        """Obtiene todos los registros de la tabla ortodoncia asociados a un cliente."""
        with SessionLocal() as session:
            return session.query(TablaOrtodoncia).filter(TablaOrtodoncia.cliente_id == cliente_id).first()

            
    @staticmethod
    def actualizar_campos(cliente_id, valores):
        """
        Actualiza múltiples campos en la tabla ortodoncia en una sola transacción.
        :param cliente_id: ID del cliente.
        :param valores: Diccionario con los campos y nuevos valores {campo: nuevo_valor}.
        """
        with SessionLocal() as session:
            registro = session.query(TablaOrtodoncia).filter(
                TablaOrtodoncia.cliente_id == cliente_id
            ).first()

            if not registro:
                registro = TablaOrtodoncia(cliente_id=cliente_id)
                session.add(registro)
            
            for campo, nuevo_valor in valores.items():
                setattr(registro, campo, nuevo_valor)
            session.commit()

