from django import forms
from . import models
from . import widgets
from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth.password_validation as validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm


# Jugador
class JugadorForm(forms.ModelForm):
    class Meta:
        model = models.Jugadores
        fields = "__all__"
        widgets = widgets.JugadorWidgets

    # El método clean() se utiliza para realizar la validación de los datos del formulario.
    # Se puede utilizar para realizar validaciones que no dependen de un solo campo.
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


# Objeto
class ObjetoForm(forms.ModelForm):
    class Meta:
        model = models.Objetos
        fields = "__all__"
        widgets = widgets.ObjetoWidgets

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data


# Inventario
class InventarioForm(forms.ModelForm):
    class Meta:
        model = models.Inventario
        fields = "__all__"
        widgets = widgets.InventarioWidgets

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
