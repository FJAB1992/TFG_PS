from django.contrib.auth.models import User
from django.db import models

# Modelo inventario de un jugador
class Inventario(models.Model):
    # Relación de muchos a uno con el modelo Jugadores
    jugador = models.ForeignKey("Jugadores", on_delete=models.CASCADE)
    # Relación de muchos a uno con el modelo Objetos
    objeto = models.ForeignKey("Objetos", on_delete=models.CASCADE)
    # Campo opcional que representa la cantidad de un objeto
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        # Nombre en singular para la representación del modelo en la administración de Django
        verbose_name = "inventario"
        # Nombre en plural para la representación del modelo en la administración de Django
        verbose_name_plural = "inventarios"
        # Nombre de la tabla en la base de datos
        db_table = "inventario"
        # Restricción de unicidad compuesta, un jugador no puede tener el mismo objeto más de una vez
        unique_together = (("jugador", "objeto"),)
        # Especifica la aplicación a la que pertenece este modelo
        app_label = "tfg_ps_app"

# Modelo jugadores
class Jugadores(models.Model):
    # Relación uno a uno con el modelo User de Django para asociar un usuario con un jugador
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Campo que representa la cantidad de dinero que tiene un jugador de manera inicial
    dinero = models.IntegerField(default=5000)

    def __str__(self):
        # Devuelve el nombre de usuario del jugador como representación en forma de cadena
        return self.user.username

    class Meta:
        # Nombre en singular para la representación del modelo en la administración de Django
        verbose_name = "jugador"
        # Nombre en plural para la representación del modelo en la administración de Django
        verbose_name_plural = "jugadores"
        # Nombre de la tabla en la base de datos
        db_table = "jugadores"
        # Especifica la aplicación a la que pertenece este modelo
        app_label = "tfg_ps_app"

# Modelo que representa los objetos disponibles en el juego
class Objetos(models.Model):
    # Campo de texto que representa el nombre del objeto
    nombre = models.CharField(max_length=50)
    # Campo de texto que representa la descripción del objeto (opcional)
    descripcion = models.TextField(blank=True, null=True)
    # Campo que representa el precio del objeto
    precio = models.IntegerField()
    # Campo que representa el tipo de objeto con opciones predefinidas
    tipo_objeto = models.CharField(
        max_length=8,
        choices=[
            ("Arma", "Arma"),
            ("Municion", "Municion"),
            ("Curacion", "Curacion"),
            ("Armadura", "Armadura"),
            ("Skin", "Skin"),
        ],
        blank=True,
        null=True,
    )
    # Campo de texto que representa la URL de la imagen del objeto (opcional)
    url_imagen = models.TextField(blank=True, null=True)

    def __str__(self):
        # Devuelve el nombre del objeto como representación en forma de cadena
        return self.nombre

    class Meta:
        # Nombre en singular para la representación del modelo en la administración de Django
        verbose_name = "objeto"
        # Nombre en plural para la representación del modelo en la administración de Django
        verbose_name_plural = "objetos"
        # Nombre de la tabla en la base de datos
        db_table = "objetos"
        # Especifica la aplicación a la que pertenece este modelo
        app_label = "tfg_ps_app"
