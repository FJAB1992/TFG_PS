from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views import generic
from . import models


# Create your views here.
def inicio_view(request):
    return render(request, "tfg_ps_app/inicio.html")


# REGISTRO, LOGIN Y LOGOUT DE DJANGO
@csrf_protect
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "tfg_ps_app/signup.html", {"form": form})


@csrf_protect
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("inicio")
    else:
        form = AuthenticationForm()
    return render(request, "tfg_ps_app/login.html", {"form": form})


class LogoutUsuario(LogoutView):
    next_page = reverse_lazy("inicio")


# VISTAS DE JUGADORES
class DetalleJugadorView(generic.ListView):
    model = models.Jugadores
    template_name = "tfg_ps_app/jugador_list.html"
    context_object_name = "jugadores"

    def get_queryset(self):
        return models.Jugadores.objects.all()


class CrearJugadorView(generic.CreateView):
    model = models.Jugadores
    form_class = models.Jugadores
    template_name = "tfg_ps_app/jugador_create.html"
    success_url = reverse_lazy("inicio")


class ActualizarJugadorView(generic.UpdateView):
    model = models.Jugadores
    form_class = models.Jugadores
    template_name = "tfg_ps_app/jugador_update.html"
    success_url = reverse_lazy("inicio")


class BorrarJugadorView(generic.DeleteView):
    model = models.Jugadores
    template_name = "tfg_ps_app/jugador_delete.html"
    success_url = reverse_lazy("inicio")


# VISTAS DE OBJETOS
class DetalleObjetosView(generic.ListView):
    model = models.Objetos
    template_name = "tfg_ps_app/objeto_list.html"
    context_object_name = "objetos"

    def get_queryset(self):
        return models.Objetos.objects.all()


class CrearObjetoView(generic.CreateView):
    model = models.Objetos
    form_class = models.Objetos
    template_name = "tfg_ps_app/objeto_create.html"
    success_url = reverse_lazy("inicio")


class ActualizarObjetoView(generic.UpdateView):
    model = models.Objetos
    form_class = models.Objetos
    template_name = "tfg_ps_app/objeto_update.html"
    success_url = reverse_lazy("inicio")


class BorrarObjetoView(generic.DeleteView):
    model = models.Objetos
    template_name = "tfg_ps_app/objeto_delete.html"
    success_url = reverse_lazy("inicio")


# VISTAS DE INVENTARIO
class DetalleInventarioView(generic.ListView):
    model = models.Inventario
    template_name = "tfg_ps_app/inventario_list.html"
    context_object_name = "inventarios"

    def get_queryset(self):
        return models.Inventario.objects.all()


class CrearInventarioView(generic.CreateView):
    model = models.Inventario
    form_class = models.Inventario
    template_name = "tfg_ps_app/inventario_create.html"
    success_url = reverse_lazy("inicio")


class ActualizarInventarioView(generic.UpdateView):
    model = models.Inventario
    form_class = models.Inventario
    template_name = "tfg_ps_app/inventario_update.html"
    success_url = reverse_lazy("inicio")


class BorrarInventarioView(generic.DeleteView):
    model = models.Inventario
    template_name = "tfg_ps_app/inventario_delete.html"
    success_url = reverse_lazy("inicio")
