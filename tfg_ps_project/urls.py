"""
URL configuration for tfg_ps_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from tfg_ps_app.views import inicio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Panel de administración
    path('tfg_ps_admin/', admin.site.urls),
    path('', include('tfg_ps_app.urls',namespace='tfg_ps_app')),
]

#CUIDAO

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
# Esto se debe a que esta configuración se encarga de servir los archivos multimedia en el entorno de desarrollo (DEBUG=True). 
# Cuando DEBUG está activado, Django sirve automáticamente los archivos estáticos y multimedia. Pero en producción, 
# estos deben ser manejados por el servidor web, como Nginx o Apache.