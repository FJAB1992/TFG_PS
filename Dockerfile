# Usa una imagen base de Python
FROM python:3.12

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias definidas en requirements.txt
RUN pip install -r requirements.txt

# Copia el contenido de tu proyecto Django al directorio de trabajo
COPY . .

# Expone el puerto 8000 para que pueda ser accesible desde fuera del contenedor
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
