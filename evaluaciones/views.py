from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import EvaluacionDiaria, Nota, TestVak
from .forms import EvaluacionDiariaForm, NotaForm, TestVakForm,TestVarkFormE
from django.contrib import messages

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

            puntajes = {
                'Visual': visual,
                'Auditivo': auditivo,
                'Lectura/Escritura': lectura,
                'Kinestésico': kinestesico
            }
            estilo_predominante = max(puntajes, key=puntajes.get)

            TestVak.objects.create(
                visual=visual,
                auditorio=auditivo,
                lectutura=lectura,
                kinestesico=kinestesico,
                estilo_predominante=estilo_predominante,
                estudiante=request.user
            )

            messages.success(request, '¡Test VARK completado! Tus resultados han sido guardados.')
            return redirect('evaluaciones:resultados_vark')  # Usar espacio de nombres
    else:
        form = TestVarkFormE()

    return render(request, 'evaluaciones/test_vark.html', {'form': form})

@login_required
def resultados_vark(request):
    test = TestVak.objects.filter(estudiante=request.user).last()
    if not test:
        messages.warning(request, 'No has realizado el test VARK.')
        return redirect('evaluaciones:realizar_test_vark')  # Usar espacio de nombres

    context = {
        'visual': test.visual,
        'auditivo': test.auditorio,
        'lectura': test.lectutura,
        'kinestesico': test.kinestesico,
        'estilo_predominante': test.estilo_predominante
    }
    return render(request, 'evaluaciones/resultados_vark.html', context)