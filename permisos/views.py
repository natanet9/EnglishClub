from django.shortcuts import render, redirect, get_object_or_404
from .models import PermisoAusencia
from .forms import PermisoAusenciaForm

def lista_permisos(request):
    permisos = PermisoAusencia.objects.all()
    return render(request, 'permisos_lista.html', {'permisos': permisos})

def crear_permiso(request):
    if request.method == 'POST':
        form = PermisoAusenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('permisos:lista_permisos')
    else:
        form = PermisoAusenciaForm()
    return render(request, 'permiso_form.html', {'form': form})
