from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    #lee las variables de entorno
    databaseUrl: str="sqlite:///./shortener.db"
    baseUrl:str="http://localhost:8000"
    
    #configuracion para pydantic-settings
    model_config=SettingsConfigDict(env_file=".env")
    
#se crea una unica instancia holi
settings=Settings()