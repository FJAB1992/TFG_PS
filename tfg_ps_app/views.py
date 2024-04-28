from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views import generic
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_POST


# Create your views here.
def inicio(request):
    return render(request, "inicio.html")


# REGISTRO, LOGIN Y LOGOUT DE DJANGO
@csrf_protect
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("tfg_ps_app:tienda")
    else:
        form = AuthenticationForm(request)

    return render(request, "login.html", {"form": form})


@csrf_protect
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("tfg_ps_app:tienda")
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})


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


@login_required
def inventario_jugador(request):
    jugador_id = request.user.id
    try:
        jugador = models.Jugadores.objects.get(user_id=jugador_id)
        # Obtiene el inventario del jugador y los tipos de objeto
        inventario = models.Inventario.objects.filter(
            jugador_id=jugador_id
        ).select_related("objeto")
        tipos = models.Objetos.objects.values("tipo_objeto").distinct()
        print(inventario)  # Agrega esta línea para verificar el inventario
        return render(
            request,
            "tienda.html",
            {"inventario": inventario, "jugador": jugador, "tipos": tipos},
        )
    except models.Jugadores.DoesNotExist:
        return HttpResponseBadRequest("No se encontró al jugador.")


@require_POST
@csrf_protect
def comprar_objeto(request, objeto_id):
    if request.method == "POST":
        jugador_id = request.user.id
        try:
            jugador = models.Jugadores.objects.get(user_id=jugador_id)
            objeto = models.Objetos.objects.get(id=objeto_id)
            if jugador.dinero >= objeto.precio:
                jugador.dinero -= objeto.precio
                jugador.save()
                inventario_objeto, created = models.Inventario.objects.get_or_create(
                    jugador=jugador, objeto=objeto
                )
                if not created:
                    inventario_objeto.cantidad += 1
                    inventario_objeto.save()
                messages.success(request, f"¡Has comprado {objeto.nombre}!")
            else:
                messages.error(
                    request, "No tienes suficiente dinero para comprar este objeto."
                )
        except models.Objetos.DoesNotExist:
            messages.error(request, "El objeto que intentas comprar no existe.")
        except models.Jugadores.DoesNotExist:
            return HttpResponseBadRequest("No se encontró al jugador.")
        return redirect("tienda.html")
    else:
        return HttpResponseBadRequest("Método no permitido")


@require_POST
@csrf_protect
def vender_objeto(request, inventario_id):
    if request.method == "POST":
        jugador_id = request.user.id
        try:
            jugador = models.Jugadores.objects.get(user_id=jugador_id)
            inventario_objeto = models.Inventario.objects.get(id=inventario_id)
            objeto = inventario_objeto.objeto
            jugador.dinero += objeto.precio
            jugador.save()
            if inventario_objeto.cantidad > 1:
                inventario_objeto.cantidad -= 1
                inventario_objeto.save()
            else:
                inventario_objeto.delete()
            messages.success(request, f"¡Has vendido {objeto.nombre}!")
        except models.Inventario.DoesNotExist:
            messages.error(request, "El objeto que intentas vender no existe.")
        except models.Jugadores.DoesNotExist:
            return HttpResponseBadRequest("No se encontró al jugador.")
        return redirect("tienda.html")
    else:
        return HttpResponseBadRequest("Método no permitido")
