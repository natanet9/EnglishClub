from django.urls import path
from .views import AsignaturaListView, AsignaturaCreateView, AsignaturaUpdateView

app_name = 'asignaturas'

urlpatterns = [
    path('', AsignaturaListView.as_view(), name='lista_asignatura'),
    path('crear/', AsignaturaCreateView.as_view(), name='crear_asignatura'),
    path('editar/<int:pk>/', AsignaturaUpdateView.as_view(), name='editar_asignatura'),
]
