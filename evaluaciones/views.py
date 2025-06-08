from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import EvaluacionDiaria, Nota, TestVak
from .forms import EvaluacionDiariaForm, NotaForm, TestVakForm

# EVALUACIÓN DIARIA
class EvaluacionDiariaListView(ListView):
    model = EvaluacionDiaria
    template_name = 'evaluaciondiaria_lista.html'
    context_object_name = 'evaluaciondiaria_list'


class EvaluacionDiariaCreateView(CreateView):
    model = EvaluacionDiaria
    form_class = EvaluacionDiariaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('evaluaciones:lista_evaluaciondiaria')

class EvaluacionDiariaUpdateView(UpdateView):
    model = EvaluacionDiaria
    form_class = EvaluacionDiariaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('evaluaciones:lista_evaluaciondiaria')

# NOTA
class NotaListView(ListView):
    model = Nota
    template_name = 'nota_lista.html'
    context_object_name = 'nota_list'

class NotaCreateView(CreateView):
    model = Nota
    form_class = NotaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('evaluaciones:lista_nota')

class NotaUpdateView(UpdateView):
    model = Nota
    form_class = NotaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('evaluaciones:lista_nota')

# TEST VAK
class TestVakListView(ListView):
    model = TestVak
    template_name = 'testvak_lista.html'
    context_object_name = 'testvak_list'

class TestVakCreateView(CreateView):
    model = TestVak
    form_class = TestVakForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('evaluaciones:lista_testvak')

class TestVakUpdateView(UpdateView):
    model = TestVak
    form_class = TestVakForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('evaluaciones:lista_testvak')
