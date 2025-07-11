from django.urls import path
from cursos.views import (
    inscripcion_list,
    inscripcion_create,
    inscripcion_edit,
    inscripcion_delete,
    curso_list,
    curso_create,
    curso_edit,
    curso_delete
)

app_name = 'cursos'

urlpatterns = [
    # Módulo de inscripciones
    path('inscripciones/', inscripcion_list, name='inscripcion_list'),
    path('inscripciones/crear/', inscripcion_create, name='inscripcion_create'),
    path('inscripciones/editar/<int:pk>/', inscripcion_edit, name='inscripcion_edit'),
    path('inscripciones/eliminar/<int:pk>/', inscripcion_delete, name='inscripcion_delete'),

    # Módulo de cursos
    path('cursos/', curso_list, name='curso_list'),
    path('cursos/crear/', curso_create, name='curso_create'),
    path('cursos/editar/<int:pk>/', curso_edit, name='curso_edit'),
    path('cursos/eliminar/<int:pk>/', curso_delete, name='curso_delete'),
]
