import random
import string
from typing import Optional
from .repository import IUrlRepository

class UrlShortenerService:
    #la dependencia se inyecta en el constructor
    def __init__(self,repository:IUrlRepository,baseUrl:str):
        self.repository=repository
        self.baseUrl=baseUrl
        
    def _generateShortCode(self,length:int=6)->str:
        #bucle para que el codigo generado sea único
        while True:
            characters=string.ascii_letters+string.digits
            shortCode=''.join(random.choice(characters)for _ in range(length))
            if self.repository.getByCode(shortCode) is None:
                return shortCode
    def createShorUrl(self,originalUrl:str)->str:
        shortCode=self._generateShortCode()
        self.repository.save(shortCode,originalUrl)
        return f"{self.baseUrl}/{shortCode}"
    def getOriginalUrl(self,shortCode:str)->Optional[str]:
        link=self.repository.getByCode(shortCode)
        return link.original_url if link else None
        