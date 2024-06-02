from django import forms


# Widgets de Jugador
class JugadorWidgets:
    # Widgets para el formulario de Jugador.
    # Define los widgets para los campos del formulario de Jugador.
    dinero = forms.NumberInput(attrs={"class": "form-control"})


# Widgets de Objeto
class ObjetoWidgets:
    # Widgets para el formulario de Objeto.
    # Define los widgets para los campos del formulario de Objeto.
    nombre = forms.TextInput(attrs={"class": "form-control"})
    descripcion = forms.Textarea(attrs={"class": "form-control", "rows": 3})
    precio = forms.NumberInput(attrs={"class": "form-control"})
    tipo_objeto = forms.TextInput(attrs={"class": "form-control"})
    imagen = forms.URLInput(attrs={"class": "form-control"})


# Widgets de Inventario
class InventarioWidgets:
    # Widgets para el formulario de Inventario.
    # Define los widgets para los campos del formulario de Inventario.
    jugador_id = forms.Select(attrs={"class": "form-control"})
    objeto_id = forms.Select(attrs={"class": "form-control"})
    cantidad = forms.NumberInput(attrs={"class": "form-control"})
