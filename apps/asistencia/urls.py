from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_asistencias, name='listar_asistencias'),
    path('nueva/', views.registrar_asistencia, name='registrar_asistencia'),
    path('editar/<int:id>/', views.editar_asistencia, name='editar_asistencia'),
    path('eliminar/<int:id>/', views.eliminar_asistencia, name='eliminar_asistencia'),
]
