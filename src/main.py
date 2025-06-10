from fastapi import FastAPI,Depends,HTTPException,Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from . import database,repository,service,config
from fastapi.middleware.cors import CORSMiddleware
#crea la tabla en la bd si no existe
database.createDatabase()

app=FastAPI(
    title="URL Shortener Microservice",
    description="A simple microservice to shorten URLs",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],)  # Permite todas las cabeceras

#Inteccion de dependencias
#dependencia pata obtener la configuracion
def getSettings()->config.Settings:
    return config.settings

#dependencia para obtener una sesión de la base de datos
def getDb():
    db=database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

#dependencia para obtener el repositorio
def getRepository(db:Session=Depends(getDb))->repository.IUrlRepository:
    return repository.SqlAlchemyRepository(db)

#dependencia para obtener el servicio de negocio
def getService(repo:repository.IUrlRepository=Depends(getRepository),
               settings:config.Settings=Depends(getSettings))->service.UrlShortenerService:
    return service.UrlShortenerService(repository=repo,baseUrl=settings.baseUrl)

#endpoints de la API

@app.post("/api/links",summary="Create a new short URL")
def createLink(originalUrl:str,svc:service.UrlShortenerService=Depends(getService)):
    #obetner una url y devolver acortada
    shortUrl=svc.createShorUrl(originalUrl)
    return {"originalUrl":originalUrl,"shortUrl":shortUrl}

@app.get("/{shortCode}",summary="Redirect to the original URL")
def redirectToUrl(shortCode:str,svc:service.UrlShortenerService=Depends(getService)):
    originalUrl=svc.getOriginalUrl(shortCode)
    if originalUrl:
        return RedirectResponse(url=originalUrl)
    raise HTTPException(status_code=404,detail="Short URL not found")

@app.get("/health",summary="Health Check")
def healthCheck():
    return{"status":"ok"}

@app.get("/api/links/{shortCode}", summary="Get original URL from a short code")
def get_link_details(shortCode: str, svc: service.UrlShortenerService = Depends(getService)):
    originalUrl = svc.getOriginalUrl(shortCode)
    if originalUrl:
        return {"shortCode": shortCode, "originalUrl": originalUrl}
    raise HTTPException(status_Code=404, detail="Short URL not found")