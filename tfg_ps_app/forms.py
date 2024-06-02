from django import forms
from . import models
from . import widgets
from django.contrib.auth.forms import UserCreationForm
import django.contrib.auth.password_validation as validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(forms.Form):
    # Formulario de inicio de sesión.
    # Permite a los usuarios ingresar sus credenciales para iniciar sesión en el sistema.
    username = forms.CharField(
        label=_("Nombre de usuario"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label=_("Contraseña"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


# Jugador
class JugadorForm(forms.ModelForm):
    # Formulario para crear o actualizar un jugador.
    # Permite a los administradores o usuarios autorizados ingresar y modificar información de los jugadores.
    class Meta:
        model = models.Jugadores
        fields = "__all__"
        widgets = widgets.JugadorWidgets

    def clean(self):
        # Método para validar los datos del formulario.
        # Este método se utiliza para realizar validaciones 
        # que no dependen de un solo campo.
        cleaned_data = super().clean()
        return cleaned_data


# Objeto
class ObjetoForm(forms.ModelForm):
    # Formulario para crear o actualizar un objeto.
    # Permite a los administradores o usuarios autorizados ingresar y modificar
    # información de los objetos disponibles en la tienda.
    class Meta:
        model = models.Objetos
        fields = "__all__"
        widgets = widgets.ObjetoWidgets

    def clean(self):
        # Método para validar los datos del formulario.
        cleaned_data = super().clean()
        return cleaned_data


# Inventario
class InventarioForm(forms.ModelForm):
    # Formulario para crear o actualizar un inventario.
    # Permite a los administradores o usuarios autorizados ingresar y modificar 
    # información sobre los objetos que un jugador posee en su inventario.
    class Meta:
        model = models.Inventario
        fields = "__all__"
        widgets = widgets.InventarioWidgets

    def clean(self):
        # Método para validar los datos del formulario.
        cleaned_data = super().clean()
        return cleaned_data
