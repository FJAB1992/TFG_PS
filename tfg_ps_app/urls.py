from django.urls import path
from .views import login_view, signup_view, LogoutUsuario, inicio
from django.contrib.auth.views import LogoutView
from . import views
from .views import DetalleObjetoView
from django.contrib.auth.decorators import login_required

app_name = "tfg_ps_app"

urlpatterns = [
    path('', views.inicio, name='inicio'),
    # Login y Registro
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", LogoutUsuario.as_view(), name='logout'),
    # Vistas detalle Objetos
    path('objetos/<int:pk>/', views.DetalleObjetoView.as_view(), name='detalle_objeto'),
    # Vista de la tienda
    path('tienda/', login_required(views.tienda), name="tienda"),
    path('vender_objeto/<int:inventario_id>/', login_required(views.vender_objeto), name='vender_objeto'),
    path('comprar_objeto/<int:objeto_id>/', login_required(views.comprar_objeto), name='comprar_objeto'),
    # Estado de la sesión
    path('check_session_status/', views.check_session_status, name='check_session_status'),
]
