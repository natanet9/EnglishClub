from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Asignatura
from .forms import AsignaturaForm

class AsignaturaListView(ListView):
    model = Asignatura
    template_name = 'asignatura_lista.html'
    context_object_name = 'asignaturas'

class AsignaturaCreateView(CreateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('asignaturas:lista_asignatura')

class AsignaturaUpdateView(UpdateView):
    model = Asignatura
    form_class = AsignaturaForm
    template_name = 'formulario.html'
    success_url = reverse_lazy('asignaturas:lista_asignatura')
