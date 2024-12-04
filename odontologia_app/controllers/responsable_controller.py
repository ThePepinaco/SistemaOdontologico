from models.database import SessionLocal
from models.responsable import Responsable
class ResponsableController:
    
    @staticmethod
    def crear_responsable(cliente_id, nombre, edad, direccion, telefono, cedula, correo):
        with SessionLocal() as session:
            nuevo_resposable = Responsable(
                cliente_id=cliente_id,
                nombre=nombre,
                edad=edad,
                direccion=direccion,
                telefono=telefono,
                cedula=cedula,
                correo=correo
            )
            session.add(nuevo_resposable)
            session.commit()


    @staticmethod
    def actualizar_responsable(cliente_id, nombre, edad, direccion, telefono, cedula, correo):
        with SessionLocal() as session:
            responsable = session.query(Responsable).filter(Responsable.cliente_id == cliente_id).first()
            if responsable:
                responsable.nombre = nombre
                responsable.edad = edad
                responsable.direccion = direccion
                responsable.telefono = telefono
                responsable.cedula = cedula
                responsable.correo = correo
                session.commit()
                
    @staticmethod
    def obtener_responsable_por_id(cliente_id):
        with SessionLocal() as session:
            return session.query(Responsable).filter(Responsable.cliente_id == cliente_id).first()
        
"""  
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
        #Busca un cliente por su cédula
        with SessionLocal() as session:
            return session.query(Cliente).filter(Cliente.cedula.ilike(f"%{cedula}%")).order_by(Cliente.nombre.asc()).all()


    @staticmethod
    def obtener_cliente_por_nombre(nombre):
        with SessionLocal() as session:
            return session.query(Cliente).filter(Cliente.nombre == nombre).first()
    """     
    
    
       

