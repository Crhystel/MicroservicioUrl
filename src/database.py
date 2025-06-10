from sqlalchemy import create_engine,Column,Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings


#configuracion del motor de base de datos
engine=create_engine(settings.databaseUrl,connect_args={"check_same_thread":False})

#creación de sesión local, cada instancia de este será una sesisón de base de datos
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

#modelos declarativos, modelos OR
Base=declarative_base()

#modelo de datos
class Link(Base):
    __tablename__="links"
    id=Column(Integer, primary_key=True,index=True)
    short_code=Column(String, unique=True,index=True,nullable=False)
    original_url=Column(String, nullable=False)
    
def createDatabase():
    Base.metadata.create_all(bind=engine)