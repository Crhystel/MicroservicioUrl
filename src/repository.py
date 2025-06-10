from abc import ABC, abstractmethod
from typing import Optional
from sqlalchemy.orm import Session
from . import database

#clase abstracta interfaz ABC
class IUrlRepository(ABC):
    @abstractmethod
    def save(self,shortCode:str,originalUrl:str)->None:
        pass
    @abstractmethod
    def getByCode(self,shortCode:str)->Optional[database.Link]:
        pass
    
   #clase que habla con una base de datos SQL a través de SQLAlchemy 
class SqlAlchemyRepository(IUrlRepository):
    #la dependencia se inyecta en el constructor
    def __init__(self,db:Session):
        self.db=db
    def save(self,shortCode:str,originalUrl:str)->None:
        db_link = database.Link(shortCode=shortCode, originalUrl=originalUrl)
        self.db.add(db_link)
        self.db.commit()
        self.db.refresh(db_link)
    def getByCode(self,shortCode:str)->Optional[database.Link]:
        return self.db.query(database.Link).filter(database.Link.shortCode==shortCode).first()