# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('paginas.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('cursos/', include('cursos.urls')),
    #path('evaluaciones/', include('evaluaciones.urls')),
]
