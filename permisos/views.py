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

    fecha = request.GET.get('fecha')
    estudiante = request.GET.get('estudiante')
    asignatura = request.GET.get('asignatura')
    curso = request.GET.get('curso')
    estado = request.GET.get('estado')

    if fecha:
        permisos = permisos.filter(fecha=fecha)
    if estudiante:
        permisos = permisos.filter(estudiante__nombre__icontains=estudiante)
    if asignatura:
        permisos = permisos.filter(asignatura__icontains=asignatura)
    if curso:
        permisos = permisos.filter(curso__icontains=curso)

    if estado == "aprobado":
        permisos = permisos.filter(aprobado=True)
    elif estado == "pendiente":
        permisos = permisos.filter(aprobado=False)

    return render(request, 'permisos_lista.html', {
        'permisos': permisos
    })

@login_required
def mis_permisos(request):
    permisos = PermisoAusencia.objects.filter(estudiante=request.user).order_by('-fecha')
    return render(request, 'mis_permisos.html', {'permisos': permisos})   
from django.contrib import messages

@login_required
def crear_permiso(request):
    if request.method == 'POST':
        form = PermisoAusenciaForm(request.POST, user=request.user)
        if form.is_valid():
            permiso = form.save(commit=False)
            permiso.estudiante = request.user
            permiso.save()
            messages.success(request, "✅ Tu solicitud de permiso fue enviada exitosamente.")
            return redirect('permisos:lista_permisos')
    else:
        form = PermisoAusenciaForm(user=request.user)
    return render(request, 'permiso_form.html', {'form': form})

@login_required
def aprobar_permiso(request, pk):
    if request.method == 'POST':
        permiso = get_object_or_404(PermisoAusencia, pk=pk)
        permiso.aprobado = True
        permiso.save()
        messages.success(request, '✅ Permiso aprobado correctamente.')
    return redirect('permisos:lista_permisos')



