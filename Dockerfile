# Imagen base oficial ligera de Python
FROM python:3.11-slim

# Evitar que Python escriba archivos .pyc y permitir logs directos en consola
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Puerto por defecto para compatibilidad con Google Cloud Run
ENV PORT=8080

# Directorio de trabajo en el contenedor
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Exponer el puerto
EXPOSE 8080

# Ejecutar el servidor gunicorn compatible con Cloud Run
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 main:app
