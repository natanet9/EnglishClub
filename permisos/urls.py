from django.urls import path
from . import views

app_name = 'permisos'

urlpatterns = [
    path('', views.lista_permisos, name='lista_permisos'),
    path('nuevo/', views.crear_permiso, name='crear_permiso'),
]
