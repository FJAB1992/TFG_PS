from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_protect
from django.views import generic
from . import models
from .models import Jugadores, Objetos, Inventario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from collections import defaultdict


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

    return render(request, "login.html", {"form": form, "user": request.user})

@csrf_protect
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crear un objeto Jugadores asociado al nuevo usuario
            jugador = Jugadores.objects.create(user=user)
            login(request, user)
            return redirect("tfg_ps_app:tienda")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form, "user": request.user})


class LogoutUsuario(LogoutView):
    next_page = reverse_lazy("tfg_ps_app:inicio")


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
class DetalleObjetoView(generic.DetailView):
    model = Objetos
    template_name = (
        "tfg_ps_app/detalle_objeto.html"  # Nombre del template de detalle de objeto
    )
    context_object_name = "objeto"  # Nombre del objeto en el contexto del template

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
def tienda(request):
    jugador_id = request.user.id
    try:
        jugador = models.Jugadores.objects.get(user_id=jugador_id)
        # Obtiene el inventario del jugador
        inventario_jugador = models.Inventario.objects.filter(
            jugador_id=jugador_id
        ).select_related("objeto")
        # Obtiene todos los objetos disponibles en la tienda
        objetos_tienda = models.Objetos.objects.all()
        tipos = models.Objetos.objects.values("tipo_objeto").distinct()
        print(
            inventario_jugador
        )  # Agrega esta línea para verificar el inventario del jugador
        print(
            objetos_tienda
        )  # Agrega esta línea para verificar los objetos disponibles en la tienda
        return render(
            request,
            "tienda.html",
            {
                "inventario_jugador": inventario_jugador,
                "objetos_tienda": objetos_tienda,
                "jugador": jugador,
                "tipos": tipos,
                "user": request.user,
            },
        )
    except models.Jugadores.DoesNotExist:
        return HttpResponseBadRequest("No se encontró al jugador.")


@require_POST
@login_required
def comprar_objeto(request, objeto_id):
    jugador_id = request.user.id
    try:
        jugador = Jugadores.objects.get(user_id=jugador_id)
        objeto = Objetos.objects.get(id=objeto_id)
        if jugador.dinero >= objeto.precio:
            jugador.dinero -= objeto.precio
            jugador.save()
            # Obtener el inventario del jugador para el objeto dado
            inventario_objeto = Inventario.objects.filter(jugador=jugador, objeto=objeto).first()
            # Verificar si ya tiene este objeto en el inventario
            if inventario_objeto:
                inventario_objeto.cantidad += 1
            else:
                # Si el jugador no tiene este objeto en el inventario, crear uno nuevo
                inventario_objeto = Inventario.objects.create(jugador=jugador, objeto=objeto, cantidad=1)
            inventario_objeto.save()
            messages.success(request, f"¡Has comprado {objeto.nombre}!")
        else:
            messages.error(
                request, "No tienes suficiente dinero para comprar este objeto."
            )
    except Objetos.DoesNotExist:
        messages.error(request, "El objeto que intentas comprar no existe.")
    except Jugadores.DoesNotExist:
        return HttpResponseBadRequest("No se encontró al jugador.")
    return redirect("tfg_ps_app:tienda")
@require_POST
@login_required
def vender_objeto(request, inventario_id):
    jugador_id = request.user.id
    try:
        jugador = Jugadores.objects.get(user_id=jugador_id)
        inventario_objeto = Inventario.objects.get(id=inventario_id)
        objeto = inventario_objeto.objeto
        jugador.dinero += objeto.precio
        jugador.save()
        # Verificar si inventario_objeto es None o no
        if inventario_objeto is not None and inventario_objeto.cantidad > 1:
            inventario_objeto.cantidad -= 1
            inventario_objeto.save()
        else:
            # Si inventario_objeto es None o la cantidad es 1, eliminar el objeto del inventario
            inventario_objeto.delete()
        messages.success(request, f"¡Has vendido {objeto.nombre}!")
    except Inventario.DoesNotExist:
        messages.error(request, "El objeto que intentas vender no existe.")
    except Jugadores.DoesNotExist:
        return HttpResponseBadRequest("No se encontró al jugador.")
    return redirect("tfg_ps_app:tienda")



# Verifica si un usuario está autenticado y devuelve un JSON con el estado de la sesión.
def check_session_status(request):
    if request.user.is_authenticated:
        return JsonResponse({"logged_in": True})
    else:
        return JsonResponse({"logged_in": False})
