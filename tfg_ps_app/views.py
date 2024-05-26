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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm(request)

    return render(request, "login.html", {"form": form, "user": request.user})


@csrf_protect
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Crea objeto Jugador asociado a la tabla de User de Django
            jugador = Jugadores.objects.create(user=user)
            login(request, user)
            return redirect("tfg_ps_app:tienda")
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form, "user": request.user})


class LogoutUsuario(LogoutView):
    next_page = reverse_lazy("tfg_ps_app:inicio")


# VISTAS DE OBJETOS
class DetalleObjetoView(generic.DetailView):
    model = Objetos
    template_name = "detalle_objeto.html" 
    context_object_name = "objeto" 

    def get_queryset(self):
        return models.Objetos.objects.all()

@login_required
def tienda(request):
    jugador_id = request.user.id
    query = request.GET.get("q", "")  # Obtener el parámetro de búsqueda
    tipo = request.GET.get("tipo", "")  # Obtener el parámetro de filtro por tipo

    try:
        jugador = models.Jugadores.objects.get(user_id=jugador_id)

        # Paginación para inventario
        inventario_jugador_list = models.Inventario.objects.filter(
            jugador=jugador
        ).select_related("objeto")
        inventario_paginator = Paginator(inventario_jugador_list, 5)
        inventario_page = request.GET.get("inventario_page")

        try:
            inventario_jugador = inventario_paginator.page(inventario_page)
        except PageNotAnInteger:
            inventario_jugador = inventario_paginator.page(1)
        except EmptyPage:
            inventario_jugador = inventario_paginator.page(
                inventario_paginator.num_pages
            )

        # Filtrar objetos de la tienda por nombre y tipo
        objetos_tienda_list = models.Objetos.objects.all()
        if query:
            objetos_tienda_list = objetos_tienda_list.filter(nombre__icontains=query)
        if tipo:
            objetos_tienda_list = objetos_tienda_list.filter(tipo_objeto=tipo)
        
        # Paginación para la tienda
        tienda_paginator = Paginator(objetos_tienda_list, 5)
        tienda_page = request.GET.get("tienda_page")

        try:
            objetos_tienda = tienda_paginator.page(tienda_page)
        except PageNotAnInteger:
            objetos_tienda = tienda_paginator.page(1)
        except EmptyPage:
            objetos_tienda = tienda_paginator.page(tienda_paginator.num_pages)

        tipos = models.Objetos.objects.values("tipo_objeto").distinct()

        return render(
            request,
            "tienda.html",
            {
                "inventario_jugador": inventario_jugador,
                "objetos_tienda": objetos_tienda,
                "jugador": jugador,
                "tipos": tipos,
                "user": request.user,
                "query": query,
                "tipo": tipo,  
            },
        )
    except models.Jugadores.DoesNotExist:
        return HttpResponseBadRequest("No se encontró al jugador.")

        return render(
            request,
            "tienda.html",
            {
                "inventario_jugador": inventario_jugador,
                "objetos_tienda": objetos_tienda,
                "jugador": jugador,
                "tipos": tipos,
                "user": request.user,
                "query": query,
                "tipo": tipo,  
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
            inventario_objeto, created = Inventario.objects.get_or_create(
                jugador=jugador, objeto=objeto
            )
            # Incrementar la cantidad si ya existe
            if not created:
                inventario_objeto.cantidad += 1
            else:
                # Si es un nuevo objeto en el inventario, inicializar la cantidad a 1
                inventario_objeto.cantidad = 1
            inventario_objeto.save()
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
