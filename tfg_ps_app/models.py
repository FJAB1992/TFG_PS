from django.contrib.auth.models import User
from django.db import models


class Inventario(models.Model):
    jugador = models.ForeignKey("Jugadores", on_delete=models.CASCADE)
    objeto = models.ForeignKey("Objetos", on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = "inventario"
        verbose_name_plural = "inventarios"
        db_table = "inventario"
        unique_together = (("jugador", "objeto"),)
        app_label = "tfg_ps_app"


class Jugadores(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dinero = models.IntegerField(default=5000)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "jugador"
        verbose_name_plural = "jugadores"
        db_table = "jugadores"
        app_label = "tfg_ps_app"


class Objetos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField()
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
    url_imagen = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "objeto"
        verbose_name_plural = "objetos"
        db_table = "objetos"
        app_label = "tfg_ps_app"