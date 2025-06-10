# Usa una imagen base de Python oficial y ligera.
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor.
WORKDIR /app

# Copia primero el archivo de requisitos para aprovechar el caché de capas de Docker.
COPY requirements.txt .

# Instala las dependencias.
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación.
COPY ./src /app/src

# Expone el puerto en el que se ejecutará la aplicación.
EXPOSE 8000

# El comando para iniciar la aplicación cuando el contenedor se ejecute.
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]