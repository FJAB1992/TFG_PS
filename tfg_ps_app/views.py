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

# Muestra la página de inicio.
def inicio(request):
    return render(request, "inicio.html")


# REGISTRO, LOGIN Y LOGOUT
# Gestiona el inicio de sesión de los usuarios. Si el método de la solicitud es POST, 
# intenta autenticar al usuario. Si es válido, inicia sesión y redirige a la tienda. 
# Si no, muestra un mensaje de error. Si el método es GET, muestra el formulario de inicio de sesión.
# Se usa el decorador csrf_protect para evitar ataques CSRF.
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

# Gestiona el registro de nuevos usuarios. Si el método de la solicitud es POST, 
# intenta crear un nuevo usuario y un objeto Jugador asociado. Si es válido, inicia sesión y redirige a la tienda. 
# Si no, muestra un mensaje de error. Si el método es GET, muestra el formulario de registro.
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

# Gestiona el cierre de sesión de los usuarios y redirige a la página de inicio.
class LogoutUsuario(LogoutView):
    next_page = reverse_lazy("tfg_ps_app:inicio")


# VISTAS DE OBJETOS
class DetalleObjetoView(generic.DetailView):
    model = Objetos
    template_name = "detalle_objeto.html" 
    context_object_name = "objeto" 

    def get_queryset(self):
        return models.Objetos.objects.all()


# VISTA DE LA TIENDA
# Este decorador asegura que solo los usuarios autenticados pueden acceder a la función tienda. 
# Si un usuario no autenticado intenta acceder, será redirigido a la página de inicio de sesión.
@login_required
def tienda(request):
    jugador_id = request.user.id
    query = request.GET.get("q", "")  # Parámetro de búsqueda por nombre
    tipo = request.GET.get("tipo", "")  # Parámetro de filtro por tipo

    try:
        jugador = models.Jugadores.objects.get(user_id=jugador_id)

        # Paginación para inventario
        # Se obtiene la lista de objetos en el inventario del jugador y se configura 
        # la paginación para mostrar 5 objetos por página. Se maneja la solicitud de 
        # la página específica y se controla si la página no es un entero válido o si está vacía.
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

        # Filtrar objetos de la tienda por nombre y tipo:
        # Se obtiene la lista de todos los objetos disponibles en la tienda. 
        # Si se proporcionan parámetros de búsqueda o filtro, se aplican a la lista de objetos. 
        # La paginación se configura para mostrar 5 objetos por página y se maneja la solicitud de la página específica.
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

        # Se obtiene una lista de tipos de objetos distintos para mostrar en la interfaz de usuario, 
        # permitiendo al jugador filtrar los objetos por tipo.
        tipos = models.Objetos.objects.values("tipo_objeto").distinct()
        
        # Se renderiza la plantilla tienda.html con el contexto necesario que incluye el 
        # inventario del jugador, los objetos disponibles en la tienda, el jugador actual, 
        # los tipos de objetos, el usuario autenticado y los parámetros de búsqueda y filtro.
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
    # Si no se encuentra al jugador en la base de datos, se retorna un error HttpResponseBadRequest.
    except models.Jugadores.DoesNotExist:
        return HttpResponseBadRequest("No se encontró al jugador.")
    

# Funcion para comprar objetos
# Estos decoradores aseguran que solo los usuarios autenticados pueden acceder a la función comprar_objeto 
# y que solo se permite el método POST. Si un usuario no autenticado intenta acceder, será redirigido a la página de inicio de sesión.
@require_POST
@login_required
def comprar_objeto(request, objeto_id):
    jugador_id = request.user.id
    try:
        jugador = Jugadores.objects.get(user_id=jugador_id)
        objeto = Objetos.objects.get(id=objeto_id)
        
        # Verifica si el jugador tiene suficiente dinero para comprar el objeto
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



# Funcion para vender objetos
# Estos decoradores aseguran que solo los usuarios autenticados pueden acceder a la función vender_objeto
# y que solo se permite el método POST. Si un usuario no autenticado intenta acceder
# se redirigirá a la página de inicio de sesión.
@require_POST
@login_required
def vender_objeto(request, inventario_id):
    jugador_id = request.user.id
    try:
        jugador = Jugadores.objects.get(user_id=jugador_id)
        inventario_objeto = Inventario.objects.get(id=inventario_id)
        objeto = inventario_objeto.objeto
        
        # Incrementar el dinero del jugador en función del precio del objeto vendido
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



# Función para verificar el estado de la sesión del usuario autenticado.
# Esta función es útil para verificar el estado de la sesión de un usuario de manera asíncrona desde el frontend,
# permitiendo saber si el usuario está logueado sin necesidad de recargar la página.
def check_session_status(request):
    if request.user.is_authenticated:
        return JsonResponse({"logged_in": True})
    else:
        return JsonResponse({"logged_in": False})
