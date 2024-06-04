# Instalar las dependencias necesarias:

```sudo yum groupinstall -y "Development Tools"```
```sudo yum install -y wget openssl-devel bzip2-devel libffi-devel zlib-devel```

# Descargar el código fuente de Python 3.12.2:

```wget https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tgz```

# Extraer el archivo descargado:

```tar -xf Python-3.12.2.tgz```
```cd Python-3.12.2```

# Compilar e instalar Python:

```./configure --enable-optimizations```
```make -j $(nproc)```
```sudo make altinstall```

# Verificar la instalación:

```python3.12 --version```

--------------------------------------------------------------------------------

# Eliminar el entorno de windows:

```rm -rf /home/ec2-user/environment/TFG_PS/.env```

# Crear el nuevo entorno:

```/home/ec2-user/environment/Python-3.12.2/python3.12 -m venv /home/ec2-user/environment/TFG_PS/.env```

# El archivo de donfiguración del entorno (pyvenv.cfg) quedaría así:

home = /home/ec2-user/environment/Python-3.12.2
include-system-site-packages = false
version = 3.12.2
executable = /home/ec2-user/environment/Python-3.12.2/python3.12
command = /home/ec2-user/environment/Python-3.12.2/python3.12 -m venv /home/ec2-user/environment/TFG_PS/.env

# Activar el Entorno Virtual:

```source /home/ec2-user/environment/TFG_PS/.env/bin/activate```

# Instalar dependencias si fuese necesario:

```pip install -r requirements.txt```

# Ejecutar proyecto:

```python manage.py runserver```