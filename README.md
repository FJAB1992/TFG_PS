# TFG
# Python web

## Preparación del entorno

  1. Crear un entorno virtual
  ```python –m venv nombre_entorno```

  2. Abrir el proyecto

  3. Activar el entorno virtual, para ello nos vamos a la carpeta Scripts y la activamos
  ```.\Scripts\activate```

  4. Intalar Django ```pip install Django```, para una versión específica ```pip install Django==5.0.1```
  ```pip install Django```

 5. Crear proyecto de Django ```django-admin startproject nombre_proyecto .```

### . No creará doble carpeta

  ```django-admin startproject nombre_proyecto . ``` 

  6. Ejecutar el proyecto Django
  ```python manage.py runserver``` 

## Crear aplicación 

```python manage.py startapp nombre```

## Base de datos

### Modificar en settings.py, base de datos

  1. Instalar cliente de Mysql
  ```pip install mysqlclient```

  2. Configurar la cadena de conexión en settings.py
  ```python
  DATABASES = {
    'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'nombre_de_la_bbdd',
      'USER': 'usuario',
      'PASSWORD': 'contraseña',
      'HOST': 'localhost',
      'PORT': '3306'
    }
  }
  ```

  3. Resolver los warnings de migración
```python manage.py migrate```
```python manage.py makemigrations```

Será necesario añadir los path de la aplicación (creados en esta), e incluirlos en el path del proyecto


### Nota:En caso de conflictos con la migración, eliminar carpeta migration y realizarla de nuevo. 

### OJO: recargar cache con: ctrl + shift +r (para  refrescar caché) o ctrl+ r (solo para actualizar)

---------------------------------------------------------------------------------------
Nota: desde el archivo pyvenv.cfg, configuramos desde donde se usa python
---------------------------------------------------------------------------------------

## Configuración de Admin

```python manage.py createsuperuser```


# Adicional
Sacar en terminal en models.py los modelos de las tablas, junto con este aviso sobre cómo usarlo: 

```python manage.py inspectdb```


Este es un módulo de modelos autogenerado de Django.
Hay que hacer lo siguiente MANUALMENTE para dejarlo limpio:
* Reordenar el orden de los modelos.
* Asegurar que cada modelo tiene un campo con primary_key=True
* Asegurar que cada ForeignKey y OneToOneField tiene `on_delete` ajustado al comportamiento que desees
* Eliminar las líneas con  `managed=False` si quieres dejar que Django cree, modifique y borre la tabla
* Renombra los modelos como gustes, pero NO renombres los valores de db_table o los campos de las tablas.


# Añadir gestión de imágenes a Django

```pip install Pillow```

## Ejecutar migraciones de nuevo

```python manage.py migrate```
```python manage.py makemigrations```

# Comando genérico para ejecutar TestCase en django

```python manage.py test nombre_de_tu_app.tests.NombreTestCase```

en este caso:

```python manage.py test tfg_ps_app.tests.TiendaTestCase```

# Eliminar todos los datos de las tablas de la base de datos
```python manage.py flush```


# Generar el archivo requirements/makefile
```pip freeze > requirements.txt```

# Instalar requirements
```pip install -r requirements.txt```


----------------------------------------------------------------
## Para despliegue con Docker

# Construir la imagen Docker
```docker build -t nombre_de_tu_imagen .```

# Ejecutar el contenedor Docker
```docker run -p 8000:8000 nombre_de_tu_imagen```


----------------------------------------------------------------
# Despliegue para ngrok

```pip install django-cors-headers```