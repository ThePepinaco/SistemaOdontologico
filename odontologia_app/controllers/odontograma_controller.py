from models.database import SessionLocal
from models.odontograma import Odontograma

class OdontogramaController:
    @staticmethod
    def obtener_por_cliente(cliente_id):
        """Obtiene todos los registros de odontograma asociados a un cliente."""
        with SessionLocal() as session:
            return session.query(Odontograma).filter(Odontograma.cliente_id == cliente_id).all()

    @staticmethod
    def agregar_o_actualizar(cliente_id, cuadro_id, color):
        """
        Agrega un nuevo registro de odontograma o actualiza uno existente para un cliente y cuadro específicos.
        :param cliente_id: ID del cliente.
        :param cuadro_id: ID del cuadro en el odontograma.
        :param color: Color asociado al cuadro en el odontograma.
        """
        with SessionLocal() as session:
            # Buscar si ya existe un registro para este cliente y cuadro
            registro = session.query(Odontograma).filter(
                Odontograma.cliente_id == cliente_id,
                Odontograma.cuadro_id == cuadro_id
            ).first()

            if registro:
                # Si existe, actualizar el color
                registro.color = color
            else:
                # Si no existe, agregar un nuevo registro
                nuevo_registro = Odontograma(cliente_id=cliente_id, cuadro_id=cuadro_id, color=color)
                session.add(nuevo_registro)

            session.commit()