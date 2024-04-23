from django.contrib import admin
from .models import Jugadores, Inventario, Objetos
from django.utils.html import format_html
from PIL import Image
from io import BytesIO

# Register your models here.

class JugadoresAdmin(admin.ModelAdmin):
    list_display = ("dinero",)

admin.site.register(Jugadores, JugadoresAdmin)

class InventarioAdmin(admin.ModelAdmin):
    list_display = ("jugador_id", "objeto_id", "cantidad")

admin.site.register(Inventario, InventarioAdmin)

class ObjetosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio", "tipo_objeto", "mostrar_imagen")

    def mostrar_imagen(self, obj):
        if obj.imagen:
            try:
                # Si la imagen se almacena en la base de datos como bytes (MEDIUMBLOB)
                with Image.open(BytesIO(obj.imagen)) as img:
                    return format_html('<img src="data:image/jpeg;base64,{}" width="100" />', img)
            except Exception as e:
                return "Error al mostrar la imagen"
        else:
            return None
    
    mostrar_imagen.short_description = "Imagen"

admin.site.register(Objetos, ObjetosAdmin)
