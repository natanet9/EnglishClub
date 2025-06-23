from django.urls import path
from . import views

app_name = 'permisos'

urlpatterns = [
    path('', views.lista_permisos, name='lista_permisos'),
    path('nuevo/', views.crear_permiso, name='crear_permiso'),
     path('mis-permisos/', views.mis_permisos, name='mis_permisos'),
         path('permisos/aprobar/<int:pk>/', views.aprobar_permiso, name='aprobar_permiso'),
  
]
