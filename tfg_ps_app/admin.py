from django.contrib import admin
from . import models

# Register your models here.


class JugadoresAdmin(admin.ModelAdmin):
    list_display = ("dinero",)


admin.site.register(models.Jugadores, JugadoresAdmin)


class InventarioAdmin(admin.ModelAdmin):
    list_display = ("jugador_id", "objeto_id", "cantidad")


admin.site.register(models.Inventario, InventarioAdmin)


class ObjetosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio", "tipo_objeto", "imagen")


admin.site.register(models.Objetos, ObjetosAdmin)
