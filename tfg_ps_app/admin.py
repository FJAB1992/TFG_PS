from django.contrib import admin
from .models import Jugadores, Inventario, Objetos
from django.utils.html import format_html

admin.site.site_header = "Administración - TFG"


class JugadoresAdmin(admin.ModelAdmin):
    list_display = ("user", "dinero")


admin.site.register(Jugadores, JugadoresAdmin)


class InventarioAdmin(admin.ModelAdmin):
    list_display = ("jugador", "objeto", "cantidad")


admin.site.register(Inventario, InventarioAdmin)


class ObjetosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio", "tipo_objeto", "mostrar_imagen")

    def mostrar_imagen(self, obj):
        if obj.url_imagen:
            return format_html('<img src="{}" width="60" height="60" />', obj.url_imagen)
        else:
            return "No hay imagen"

    mostrar_imagen.short_description = "Imagen"


admin.site.register(Objetos, ObjetosAdmin)
