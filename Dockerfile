# Imagen oficial de Python para Django
FROM python:3.12

# Establecer las variables de entorno para Python y el sistema operativo
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo requirements.txt al directorio de trabajo
COPY requirements.txt /app/

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto al directorio de trabajo
COPY . /app/

# Puerto en el que Django se ejecutará dentro del contenedor
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
