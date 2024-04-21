from django.urls import path
from .views import login_view, signup_view
from django.contrib.auth.views import LogoutView
from . import views

app_name = "tfg_ps_app"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # Login y Registro
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path('logout/', views.LogoutUsuario.as_view(), name='logout'),
    # Vistas de jugadores
    path("jugadores/", views.DetalleJugadorView.as_view(), name="jugadores"),
    path("jugadores/crear/", views.CrearJugadorView.as_view(), name="jugadores_crear"),
    path("jugadores/editar/<int:pk>/", views.ActualizarJugadorView.as_view(), name="jugadores_editar"),
    path("jugadores/borrar/<int:pk>/", views.BorrarJugadorView.as_view(), name="jugadores_borrar"),
    # Vistas de Objetos
    path('objetos/', views.DetalleObjetosView.as_view(), name="objetos"),
    path('objetos/crear/', views.CrearObjetoView.as_view(), name="objetos_crear"),
    path('objetos/editar/<int:pk>/', views.ActualizarObjetoView.as_view(), name="objetos_editar"),
    path('objetos/borrar/<int:pk>/', views.BorrarObjetoView.as_view(), name="objetos_borrar"),
    # Vistas de Inventario
    path('inventario/', views.DetalleInventarioView.as_view(), name="inventario"),
    path('inventario/crear/', views.CrearInventarioView.as_view(), name="inventario_crear"),
    path('inventario/editar/<int:pk>/', views.ActualizarInventarioView.as_view(), name="inventario_editar"),
    path('inventario/borrar/<int:pk>/', views.BorrarInventarioView.as_view(), name="inventario_borrar"),
    
]
