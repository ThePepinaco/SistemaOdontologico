from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost/odontologia"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    # Importar los modelos para crear las tablas
    from models.cliente import Cliente
    from models.ficha_odontologica import FichaOdontologica
    from models.ficha_ortodoncia import FichaOrtodoncia
    from models.informacion_ortodoncia import InformacionOrtodoncia
    from models.tabla_ortodoncia import TablaOrtodoncia
    from models.responsable import Responsable
    from models.odontograma import Odontograma
    Base.metadata.create_all(bind=engine)
