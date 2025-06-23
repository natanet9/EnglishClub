from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import EvaluacionDiaria, Nota, TestVak
from .forms import EvaluacionDiariaForm, NotaForm, TestVakForm, TestVarkFormE, FiltroEvaluacionDiariaForm, FiltroNotaForm,FiltroTestVakForm
from django.contrib import messages
from .ml_utils import predecir_recurso
import csv
import random

# EVALUACIÓN DIARIA
class EvaluacionDiariaListView(ListView):
    model = EvaluacionDiaria
    template_name = 'evaluaciondiaria_lista.html'
    context_object_name = 'evaluaciondiaria_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modo_edicion'] = self.request.GET.get('editar') == '1'
        context['filtro_form'] = FiltroEvaluacionDiariaForm(self.request.GET or None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = FiltroEvaluacionDiariaForm(self.request.GET or None)
        if form.is_valid():
            if form.cleaned_data['estudiante']:
                queryset = queryset.filter(estudiante=form.cleaned_data['estudiante'])
            if form.cleaned_data['curso']:
                queryset = queryset.filter(curso=form.cleaned_data['curso'])
            if form.cleaned_data['asignatura']:
                queryset = queryset.filter(asignatura=form.cleaned_data['asignatura'])
            if form.cleaned_data['fecha_inicio']:
                queryset = queryset.filter(fecha__gte=form.cleaned_data['fecha_inicio'])
            if form.cleaned_data['fecha_fin']:
                queryset = queryset.filter(fecha__lte=form.cleaned_data['fecha_fin'])
            if form.cleaned_data['presente']:
                presente = form.cleaned_data['presente'] == '1'
                queryset = queryset.filter(is_present=presente)
            if form.cleaned_data['participacion_min']:
                queryset = queryset.filter(is_participate__gte=form.cleaned_data['participacion_min'])
            if form.cleaned_data['tarea_min']:
                queryset = queryset.filter(is_tarea__gte=form.cleaned_data['tarea_min'])
        return queryset

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

# NOTA
class NotaListView(ListView):
    model = Nota
    template_name = 'nota_lista.html'
    context_object_name = 'nota_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro_form'] = FiltroNotaForm(self.request.GET or None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = FiltroNotaForm(self.request.GET or None)
        if form.is_valid():
            if form.cleaned_data['estudiante']:
                queryset = queryset.filter(estudiante=form.cleaned_data['estudiante'])
            if form.cleaned_data['asignatura']:
                queryset = queryset.filter(asignatura=form.cleaned_data['asignatura'])
            if form.cleaned_data['nota_acumulada_min'] is not None:
                queryset = queryset.filter(nota_acumulada__gte=form.cleaned_data['nota_acumulada_min'])
            if form.cleaned_data['nota_acumulada_max'] is not None:
                queryset = queryset.filter(nota_acumulada__lte=form.cleaned_data['nota_acumulada_max'])
            if form.cleaned_data['primer_examen_min'] is not None:
                queryset = queryset.filter(primer_examen__gte=form.cleaned_data['primer_examen_min'])
            if form.cleaned_data['primer_examen_max'] is not None:
                queryset = queryset.filter(primer_examen__lte=form.cleaned_data['primer_examen_max'])
            if form.cleaned_data['segundo_examen_min'] is not None:
                queryset = queryset.filter(segundo_examen__gte=form.cleaned_data['segundo_examen_min'])
            if form.cleaned_data['segundo_examen_max'] is not None:
                queryset = queryset.filter(segundo_examen__lte=form.cleaned_data['segundo_examen_max'])
            if form.cleaned_data['examen_final_min'] is not None:
                queryset = queryset.filter(examen_final__gte=form.cleaned_data['examen_final_min'])
            if form.cleaned_data['examen_final_max'] is not None:
                queryset = queryset.filter(examen_final__lte=form.cleaned_data['examen_final_max'])
        return queryset

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtro_form'] = FiltroTestVakForm(self.request.GET or None)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = FiltroTestVakForm(self.request.GET or None)
        if form.is_valid():
            if form.cleaned_data['estudiante']:
                queryset = queryset.filter(estudiante=form.cleaned_data['estudiante'])
            if form.cleaned_data['estilo_predominante']:
                queryset = queryset.filter(estilo_predominante__iexact=form.cleaned_data['estilo_predominante'])
            if form.cleaned_data['visual_min'] is not None:
                queryset = queryset.filter(visual__gte=form.cleaned_data['visual_min'])
            if form.cleaned_data['visual_max'] is not None:
                queryset = queryset.filter(visual__lte=form.cleaned_data['visual_max'])
            if form.cleaned_data['auditorio_min'] is not None:
                queryset = queryset.filter(auditorio__gte=form.cleaned_data['auditorio_min'])
            if form.cleaned_data['auditorio_max'] is not None:
                queryset = queryset.filter(auditorio__lte=form.cleaned_data['auditorio_max'])
            if form.cleaned_data['lectutura_min'] is not None:
                queryset = queryset.filter(lectutura__gte=form.cleaned_data['lectutura_min'])
            if form.cleaned_data['lectutura_max'] is not None:
                queryset = queryset.filter(lectutura__lte=form.cleaned_data['lectutura_max'])
            if form.cleaned_data['kinestesico_min'] is not None:
                queryset = queryset.filter(kinestesico__gte=form.cleaned_data['kinestesico_min'])
            if form.cleaned_data['kinestesico_max'] is not None:
                queryset = queryset.filter(kinestesico__lte=form.cleaned_data['kinestesico_max'])
        return queryset
    
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

            recurso_recomendado = predecir_recurso(
                visual=visual,
                auditivo=auditivo,
                lectura=lectura,
                kinestesico=kinestesico
            )

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

@login_required
def resultados_vark(request):
    test = TestVak.objects.filter(estudiante=request.user).last()
    if not test:
        messages.warning(request, 'No has realizado el test VARK.')
        return redirect('evaluaciones:realizar_test_vark')

    estilo = test.estilo_predominante
    recomendaciones = []

    with open('Analisis/recomendaciones.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        recomendaciones_filtradas = [row['recomendacion'] for row in reader if row['metodo'] == estilo]

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