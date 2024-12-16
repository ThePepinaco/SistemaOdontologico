from models.database import SessionLocal
from models.ficha_odontologica import FichaOdontologica
from models.cliente import Cliente
class FichaOdontologicaController:
    
    @staticmethod
    def crear_ficha(cliente_id, fecha, tratamiento_realizado, costo, abono=0.0, saldo=0.0):
        """Crea una nueva ficha odontológica."""
        with SessionLocal() as session:
            nueva_ficha = FichaOdontologica(
                cliente_id=cliente_id,
                fecha=fecha,
                tratamiento_realizado=tratamiento_realizado,
                costo=costo,
                abono=abono,
                saldo=saldo
            )
            session.add(nueva_ficha)
            session.commit()
            FichaOdontologicaController.actualizar_saldo_total(session, cliente_id)

    @staticmethod
    def actualizar_ficha(ficha_id, fecha=None, tratamiento_realizado=None, costo=None, abono=None, saldo=None):
        """Actualiza los datos de una ficha odontológica existente."""
        with SessionLocal() as session:
            ficha = session.query(FichaOdontologica).filter(FichaOdontologica.id == ficha_id).first()
            if ficha:
                if fecha is not None:
                    ficha.fecha = fecha
                if tratamiento_realizado is not None:
                    ficha.tratamiento_realizado = tratamiento_realizado
                if costo is not None:
                    ficha.costo = costo
                if abono is not None:
                    ficha.abono = abono
                if saldo is not None:
                    ficha.saldo = saldo
                session.commit()
                FichaOdontologicaController.actualizar_saldo_total(session, ficha.cliente_id)
    @staticmethod
    def obtener_ficha_por_id(ficha_id):
        """Obtiene una ficha odontológica específica por su ID."""
        with SessionLocal() as session:
            return session.query(FichaOdontologica).filter(FichaOdontologica.id == ficha_id).first()

    @staticmethod
    def obtener_fichas_por_cliente(cliente_id):
        """Obtiene todas las fichas odontológicas asociadas a un cliente específico, ordenadas por fecha (más cercana primero)."""
        with SessionLocal() as session:
            return session.query(FichaOdontologica)\
                .filter(FichaOdontologica.cliente_id == cliente_id)\
                .order_by(FichaOdontologica.fecha.desc())\
                .all()
            


    @staticmethod
    def eliminar_ficha(ficha_id):
        """Elimina una ficha odontológica por su ID."""
        with SessionLocal() as session:
            ficha = session.query(FichaOdontologica).filter(FichaOdontologica.id == ficha_id).first()
            if ficha:
                session.delete(ficha)
                session.commit()
                FichaOdontologicaController.actualizar_saldo_total(session, ficha.cliente_id)
                

    @staticmethod
    def actualizar_saldo_total(session, cliente_id):
        """Calcula y actualiza el saldo total del cliente."""
        cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
        if cliente:
            saldo_total = session.query(FichaOdontologica)\
                .filter(FichaOdontologica.cliente_id == cliente_id)\
                .with_entities(
                    (FichaOdontologica.abono - FichaOdontologica.costo).label("saldo")
                )\
                .all()
            # Calcular el saldo total sumando los saldos de todas las fichas
            cliente.saldo_total_od = sum(s.saldo or 0 for s in saldo_total)
            session.commit()