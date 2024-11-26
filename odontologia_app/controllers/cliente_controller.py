from models.database import SessionLocal
from models.cliente import Cliente

class ClienteController:
    @staticmethod
    def crear_cliente(nombre, edad, direccion, telefono, cedula, alergias, hemorragias, problemas_cardiacos, diabetes, hipertension, anemia, alergia_medicamentos, embarazo, anestesia_previa, medicamentos):
        with SessionLocal() as session:
            nuevo_cliente = Cliente(
                nombre=nombre,
                edad=edad,
                direccion=direccion,
                telefono=telefono,
                cedula=cedula,
                alergias=alergias,
                hemorragias=hemorragias,
                problemas_cardiacos=problemas_cardiacos,
                diabetes=diabetes,
                hipertension=hipertension,
                anemia=anemia,
                alergia_medicamentos=alergia_medicamentos,
                embarazo=embarazo,
                anestesia_previa=anestesia_previa,
                medicamentos=medicamentos,
            )
            session.add(nuevo_cliente)
            session.commit()


    @staticmethod
    def actualizar_cliente(cliente_id, nombre, edad, direccion, telefono, cedula, alergias, hemorragias, problemas_cardiacos, diabetes, hipertension, anemia, alergia_medicamentos, embarazo, anestesia_previa, medicamentos):
        with SessionLocal() as session:
            cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()
            if cliente:
                cliente.nombre = nombre
                cliente.edad = edad
                cliente.direccion = direccion
                cliente.telefono = telefono
                cliente.cedula = cedula
                cliente.alergias = alergias
                cliente.hemorragias = hemorragias
                cliente.problemas_cardiacos = problemas_cardiacos
                cliente.diabetes = diabetes
                cliente.hipertension = hipertension
                cliente.anemia = anemia
                cliente.alergia_medicamentos = alergia_medicamentos
                cliente.embarazo = embarazo
                cliente.anestesia_previa = anestesia_previa
                cliente.medicamentos = medicamentos
                session.commit()

    
    @staticmethod
    def obtener_clientes():
        with SessionLocal() as session:
            return session.query(Cliente).order_by(Cliente.nombre.asc()).all()

    @staticmethod
    def buscar_por_nombre(nombre):
        with SessionLocal() as session:
            return session.query(Cliente).filter(Cliente.nombre.ilike(f"%{nombre}%")).order_by(Cliente.nombre.asc()).all()

    @staticmethod
    def buscar_por_cedula(cedula):
        """Busca un cliente por su cédula."""
        with SessionLocal() as session:
            return session.query(Cliente).filter(Cliente.cedula.ilike(f"%{cedula}%")).order_by(Cliente.nombre.asc()).all()


    @staticmethod
    def obtener_cliente_por_nombre(nombre):
        with SessionLocal() as session:
            return session.query(Cliente).filter(Cliente.nombre == nombre).first()
    @staticmethod
    def obtener_cliente_por_id(cliente_id):
        with SessionLocal() as session:
            return session.query(Cliente).filter(Cliente.id == cliente_id).first()

