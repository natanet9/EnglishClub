from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Inscripcion, Curso
from .forms import InscripcionForm, CursoForm
from django.utils import timezone

#validar si tiene accesos (rol secretario o directivo)
def is_secretaria_or_directivo(user):
    return user.is_authenticated and user.rol in ['secretaria', 'directivo']

def is_directivo(user):
    return user.is_authenticated and user.rol == 'directivo'

def is_secretaria_or_directivo_or_docente(user):
    return user.is_authenticated and user.rol in ['secretaria', 'directivo', 'docente']


#modulo inscripcion
@login_required
@user_passes_test(is_secretaria_or_directivo)
def inscripcion_list(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'Inscripcion/inscripcion_list.html', {'inscripciones': inscripciones})

@login_required
@user_passes_test(is_secretaria_or_directivo)
def inscripcion_create(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)
            if not inscripcion.fecha_inscripcion:
                inscripcion.fecha_inscripcion = timezone.now()
            inscripcion.save()
            messages.success(request, 'Inscripción creada con éxito.')
            return redirect('cursos:inscripcion_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = InscripcionForm()
    return render(request, 'Inscripcion/inscripcion_form.html', {'form': form})

@login_required
@user_passes_test(is_directivo)
def inscripcion_edit(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscripción actualizada con éxito.')
            return redirect('inscripcion_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = InscripcionForm(instance=inscripcion)
    return render(request, 'Inscripcion/inscripcion_edit.html', {'form': form, 'inscripcion': inscripcion})

@login_required
@user_passes_test(is_directivo)
def inscripcion_delete(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    if request.method == 'POST':
        inscripcion.delete()
        messages.success(request, 'Inscripción eliminada con éxito.')
        return redirect('inscripcion_list')
    return render(request, 'Inscripcion/inscripcion_confirm_delete.html', {'inscripcion': inscripcion})

#Modulo Curso
@login_required
@user_passes_test(is_secretaria_or_directivo_or_docente)
def curso_list(request):
    query = request.GET.get("q")
    cursos = Curso.objects.all()

    if query:
        cursos = cursos.filter(docente__nombre__icontains=query)
    return render(request, 'Cursos/curso_list.html', {'cursos': cursos})

@login_required
@user_passes_test(is_secretaria_or_directivo)
def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso creado con éxito.')
            return redirect('curso_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = CursoForm()
    return render(request, 'Cursos/curso_form.html', {'form': form})

@login_required
@user_passes_test(is_directivo)
def curso_edit(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso actualizado con éxito.')
            return redirect('curso_list')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'Cursos/curso_edit.html', {'form': form, 'curso': curso})

@login_required
@user_passes_test(is_directivo)
def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso eliminado con éxito.')
        return redirect('curso_list')
    return render(request, 'Cursos/curso_confirm_delete.html', {'curso': curso})

