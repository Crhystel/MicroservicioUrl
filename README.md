Este proyecto es un microservicio desarrollado en Python con FastAPI, diseñado para acortar URLs largas

## Caractaristicas
- API RESTful
- Base de datos
- Inyeccion de dependencias
- Despliegue con Docker

## Recursos utilizados
- Python
- FastAPI
- Uvicorn: como servidor ASGI
- SQLAlchemy: para ORM e interacción con bd
- Pydantic: validación de datos
- Docker

## Ejecución
Tienes dos maneras de ejecutar este proyecto: localmente para desarrollo o dentro de un contenedor de Docker.

# Crea y activa un entorno virtual
En Windows:

python -m venv .venv
.venv\Scripts\activate

En macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
- pip install -r requirements.txt
# Crear el archivo de configuracion .env
Crea un archivo llamado .env en la raíz del proyecto y añade el siguiente contenido. Este archivo es ignorado por Git y contiene la configuración específica de tu entorno.

URL de conexión para la base de datos local
DATABASE_URL="......"

URL base que usará el servicio para construir las URLs acortadas
BASE_URL="http://localhost:tu puerto"

# Ejecutar el servidor
En la terminal ejecuta el siguiente comando:
- uvicorn src.main:app --reload

## Opción 2: Ejección con Docker

Asegúrate de que Docker esté corriendo
# Construye la imagen de Docker
Este comando lee el Dockerfile y empaqueta tu aplicación en una imagen.
- docker build -t url-shortener-service .
# Ejecuta el contenedor
Este comando crea e inicia un contenedor a partir de la imagen que acabas de construir.
- docker run -d -p puerto configurado en tu .env:puerto configurado en tu .env --name shortener-app url-shortener-service

## Uso de API (Endpoints)
Para explorar e interactuar con la API de forma sencilla, visita la documentación autogenerada por Swagger UI. Simplemente abre tu navegador y ve a:

http://localhost:tu puerto/docs

## Endpoints funcionales
# POST /api/links

Descripción: Crea una nueva URL corta.

Body (payload): Debes enviar la originalUrl como un parámetro de consulta (query parameter).

Respuesta Exitosa: Un JSON con la URL original y la nueva URL corta.

{
  "original_url": "https://www.google.com",
  "short_url": "http://localhost:8000/aB1cdeF"
}

# GET /{short_code}

Descripción: Redirige a la URL original. Este endpoint está diseñado para ser usado directamente en la barra de direcciones del navegador.

Ejemplo: Si visitas http://localhost:8000/aB1cdeF, serás redirigido a https://www.google.com.

# GET /api/links/{short_code}

Descripción: Obtiene los detalles de una URL corta sin redirigir. Es útil para consultar la información de un enlace.

Respuesta Exitosa: Un JSON con el código corto y la URL original.

{
  "short_code": "aB1cdeF",
  "original_url": "https://www.google.com"
}

# GET /health

Descripción: Un endpoint de chequeo de salud. Esencial para sistemas de monitoreo.

Respuesta Exitosa:

{
  "status": "ok"
}