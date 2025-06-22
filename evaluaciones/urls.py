from django.urls import path
from .views import (
    EvaluacionDiariaListView, EvaluacionDiariaCreateView, EvaluacionDiariaUpdateView,
    NotaListView, NotaCreateView, NotaUpdateView,
    TestVakListView, TestVakCreateView, TestVakUpdateView, resultados_vark, realizar_test_vark
)

app_name = 'evaluaciones'

urlpatterns = [
    # Evaluacion Diaria
    path('evaluaciones/', EvaluacionDiariaListView.as_view(), name='lista_evaluaciondiaria'),
    path('evaluaciones/crear/', EvaluacionDiariaCreateView.as_view(), name='crear_evaluaciondiaria'),
    path('evaluaciones/editar/<int:pk>/', EvaluacionDiariaUpdateView.as_view(), name='editar_evaluaciondiaria'),

    # Nota
    path('notas/', NotaListView.as_view(), name='lista_nota'),
    path('notas/crear/', NotaCreateView.as_view(), name='crear_nota'),
    path('notas/editar/<int:pk>/', NotaUpdateView.as_view(), name='editar_nota'),

    # Test VAK
    path('testvak/', TestVakListView.as_view(), name='lista_testvak'),
    path('testvak/crear/', TestVakCreateView.as_view(), name='crear_testvak'),
    path('testvak/editar/<int:pk>/', TestVakUpdateView.as_view(), name='editar_testvak'),
    path('test-vark/', realizar_test_vark, name='realizar_test_vark'),
    path('resultados-vark/', resultados_vark, name='resultados_vark'),
]