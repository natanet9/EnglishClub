# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('paginas.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('cursos/', include('cursos.urls')),
    path('evaluaciones/', include('evaluaciones.urls')),
    path('asignaturas/', include('asignaturas.urls')),
    path('permisos/', include('permisos.urls')),

    # EnglishClub/urls.py
    path('reportes/', include('reporteria.urls')),


]
