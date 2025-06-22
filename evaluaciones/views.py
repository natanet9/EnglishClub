from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import EvaluacionDiaria, Nota, TestVak
from .forms import EvaluacionDiariaForm, NotaForm, TestVakForm,TestVarkFormE
from django.contrib import messages
from .ml_utils import predecir_recurso


# EVALUACIÓN DIARIA
class EvaluacionDiariaListView(ListView):
    model = EvaluacionDiaria
    template_name = 'evaluaciondiaria_lista.html'
    context_object_name = 'evaluaciondiaria_list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aquí capturamos el modo edición desde la URL ?editar=1
        context['modo_edicion'] = self.request.GET.get('editar') == '1'
        return context

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


@login_required
def guardar_lista_evaluaciones(request):
    if request.method == 'POST':
        ids = request.POST.getlist('evaluaciones_ids')
        for eval_id in ids:
            try:
                evaluacion = EvaluacionDiaria.objects.get(pk=eval_id)

                def limpiar_entero(valor, default=0):
                    try:
                        v = int(valor)
                        return max(0, min(10, v))  # Limita entre 0 y 10
                    except (ValueError, TypeError):
                        return default

                participacion = limpiar_entero(request.POST.get(f'participacion_{eval_id}'), evaluacion.is_participate)
                tarea = limpiar_entero(request.POST.get(f'tarea_{eval_id}'), evaluacion.is_tarea)
                presente = f'presente_{eval_id}' in request.POST

                evaluacion.is_participate = participacion
                evaluacion.is_tarea = tarea
                evaluacion.is_present = presente
                evaluacion.save()
            except EvaluacionDiaria.DoesNotExist:
                continue

    messages.success(request, "Cambios guardados correctamente.")
    return redirect('evaluaciones:lista_evaluaciondiaria')

@login_required
def lista_evaluaciondiaria(request):
    evaluaciones = EvaluacionDiaria.objects.all()
    modo_edicion = request.GET.get('editar') == '1'  # 👈 activa si hay ?editar=1
    context = {
        'evaluaciondiaria_list': evaluaciones,
        'modo_edicion': modo_edicion,
    }
    return render(request, 'evaluaciones/lista.html', context)


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

@login_required
def realizar_test_vark(request):
    if request.method == 'POST':
        form = TestVarkFormE(request.POST)
        if form.is_valid():
            visual = 0
            auditivo = 0
            lectura = 0
            kinestesico = 0

            for i in range(1, 17):  # 16 preguntas
                respuesta = form.cleaned_data.get(f'pregunta_{i}')
                if respuesta == 'visual':
                    visual += 1
                elif respuesta == 'auditivo':
                    auditivo += 1
                elif respuesta == 'lectura':
                    lectura += 1
                elif respuesta == 'kinestesico':
                    kinestesico += 1

            # Llamar al modelo para predecir el recurso
            recurso_recomendado = predecir_recurso(
                visual=visual,
                auditivo=auditivo,
                lectura=lectura,
                kinestesico=kinestesico
            )

            # Guardar en la base de datos
            TestVak.objects.create(
                visual=visual,
                auditorio=auditivo,
                lectutura=lectura,
                kinestesico=kinestesico,
                estilo_predominante=recurso_recomendado,
                estudiante=request.user
            )

            messages.success(request, '¡Test VARK completado! Tus resultados han sido guardados.')
            return redirect('evaluaciones:resultados_vark')
    else:
        form = TestVarkFormE()

    return render(request, 'evaluaciones/test_vark.html', {'form': form})

import csv
import random

@login_required
def resultados_vark(request):
    test = TestVak.objects.filter(estudiante=request.user).last()
    if not test:
        messages.warning(request, 'No has realizado el test VARK.')
        return redirect('evaluaciones:realizar_test_vark')

    estilo = test.estilo_predominante
    recomendaciones = []

    # Leer el archivo CSV y filtrar por estilo predominante
    with open('Analisis/recomendaciones.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        recomendaciones_filtradas = [row['recomendacion'] for row in reader if row['metodo'] == estilo]

    # Seleccionar entre 2 y 5 recomendaciones aleatorias
    if recomendaciones_filtradas:
        recomendaciones = random.sample(recomendaciones_filtradas, min(len(recomendaciones_filtradas), 5))

    context = {
        'visual': test.visual,
        'auditivo': test.auditorio,
        'lectura': test.lectutura,
        'kinestesico': test.kinestesico,
        'recurso': estilo,
        'recomendaciones': recomendaciones
    }
    return render(request, 'evaluaciones/resultados_vark.html', context)