from django.urls import path
from .views import login_view, signup_view, LogoutUsuario, inicio, DetalleObjetoView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from . import views

app_name = "tfg_ps_app"

urlpatterns = [
    # Ruta para la página de inicio
    path('', views.inicio, name='inicio'),
    
    # Rutas para el inicio de sesión y el registro de usuarios
    path("login/", login_view, name="login"),  # Ruta para la vista de inicio de sesión
    path("signup/", signup_view, name="signup"),  # Ruta para la vista de registro
    path("logout/", LogoutUsuario.as_view(), name='logout'),  # Ruta para la vista de cierre de sesión
    
    # Rutas para las vistas de detalle de los objetos
    path('objetos/<int:pk>/', views.DetalleObjetoView.as_view(), name='detalle_objeto'),  # Ruta para la vista de detalle de un objeto
    
    # Rutas para la vista de la tienda y acciones de compra/venta de objetos
    path('tienda/', login_required(views.tienda), name="tienda"),  # Ruta para la vista de la tienda, requiere inicio de sesión
    path('vender_objeto/<int:inventario_id>/', login_required(views.vender_objeto), name='vender_objeto'),  # Ruta para vender un objeto, requiere inicio de sesión
    path('comprar_objeto/<int:objeto_id>/', login_required(views.comprar_objeto), name='comprar_objeto'),  # Ruta para comprar un objeto, requiere inicio de sesión
    
    # Ruta para verificar el estado de la sesión
    path('check_session_status/', views.check_session_status, name='check_session_status'),  # Ruta para verificar el estado de la sesión
]
