from django.contrib import admin
from .models import Jugadores, Inventario, Objetos
from django.utils.html import format_html

# Personalización del encabezado del sitio de administración
admin.site.site_header = "Administración - TFG"

# Configuración del modelo Jugadores en el sitio de administración
class JugadoresAdmin(admin.ModelAdmin):
    # Definición de los campos que se mostrarán en la lista de Jugadores
    list_display = ("jugador", "dinero")

    # Método para obtener el nombre de usuario del jugador
    def jugador(self, obj):
        return obj.user.username
    jugador.short_description = 'Jugador'  # Descripción del campo en la lista de administración

# Registro del modelo Jugadores con su configuración personalizada
admin.site.register(Jugadores, JugadoresAdmin)

# Configuración del modelo Inventario en el sitio de administración
class InventarioAdmin(admin.ModelAdmin):
    # Definición de los campos que se mostrarán en la lista de Inventario
    list_display = ("jugador", "objeto", "cantidad")

    # Método para obtener el nombre de usuario del jugador asociado al inventario
    def jugador(self, obj):
        return obj.jugador.user.username
    jugador.short_description = 'Jugador'  # Descripción del campo en la lista de administración

# Registro del modelo Inventario con su configuración personalizada
admin.site.register(Inventario, InventarioAdmin)

# Configuración del modelo Objetos en el sitio de administración
class ObjetosAdmin(admin.ModelAdmin):
    # Definición de los campos que se mostrarán en la lista de Objetos
    list_display = ("nombre", "descripcion", "precio", "tipo_objeto", "mostrar_imagen")

    # Método para mostrar una imagen en la lista de administración
    def mostrar_imagen(self, obj):
        if obj.url_imagen:
            return format_html('<img src="{}" width="60" height="60" />', obj.url_imagen)
        else:
            return "No hay imagen"
    mostrar_imagen.short_description = "Imagen"  # Descripción del campo en la lista de administración

# Registro del modelo Objetos con su configuración personalizada
admin.site.register(Objetos, ObjetosAdmin)
