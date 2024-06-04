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
