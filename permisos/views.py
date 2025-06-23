from django.shortcuts import render, redirect, get_object_or_404
from .models import PermisoAusencia
from .forms import PermisoAusenciaForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from cursos.models import Inscripcion
from datetime import date

def lista_permisos(request):
    permisos = PermisoAusencia.objects.all()
    return render(request, 'permisos_lista.html', {'permisos': permisos})
    
@login_required
def crear_permiso(request):
    try:
        inscripcion = request.user.inscripciones_como_estudiante.latest('fecha_inscripcion')
        curso_estudiante = inscripcion.curso
    except Inscripcion.DoesNotExist:
        curso_estudiante = None

    if request.method == 'POST':
        form = PermisoAusenciaForm(request.POST)
        if form.is_valid():
            permiso = form.save(commit=False)
            permiso.estudiante = request.user
            if curso_estudiante:
                permiso.curso = curso_estudiante
            permiso.save()
            return redirect('permisos:lista_permisos')
    else:
        form = PermisoAusenciaForm()
        form.fields['estudiante'].widget = forms.HiddenInput()
        form.fields['curso'].widget = forms.HiddenInput()
        form.initial['estudiante'] = request.user.pk
        if curso_estudiante:
            form.initial['curso'] = curso_estudiante.pk
        form.initial['fecha'] = date.today()  # Aquí pones la fecha por defecto

    return render(request, 'permiso_form.html', {
        'form': form,
        'estudiante_nombre': request.user or request.user.username,
        'curso_nombre': curso_estudiante if curso_estudiante else 'Sin curso asignado'
    })

