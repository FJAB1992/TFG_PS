from django import forms


class JugadorWidgets:
    dinero = forms.NumberInput(attrs={"class": "form-control"})


class ObjetoWidgets:
    nombre = forms.TextInput(attrs={"class": "form-control"})
    descripcion = forms.Textarea(attrs={"class": "form-control", "rows": 3})
    precio = forms.NumberInput(attrs={"class": "form-control"})
    tipo_objeto = forms.TextInput(attrs={"class": "form-control"})
    imagen = forms.URLInput(attrs={"class": "form-control"})


class InventarioWidgets:
    jugador_id = forms.Select(attrs={"class": "form-control"})
    objeto_id = forms.Select(attrs={"class": "form-control"})
    cantidad = forms.NumberInput(attrs={"class": "form-control"})
