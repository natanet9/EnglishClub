from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Vista para la página de inicio
def inicio(request):
    return render(request, 'info/inicio.html')

# Vista para la página ¿Quiénes Somos?
def quienes_somos(request):
    return render(request, 'info/quienes_somos.html')

# Vista para la página de Servicios
def servicios(request):
    return render(request, 'info/servicios.html')

# Vista para la página de Contacto
def contacto(request):
    return render(request, 'info/contacto.html')


@login_required
def dash_directivo(request):
    nombre_usuario = request.user.nombre  # O request.user.username si no usas first_name
    return render(request, 'dasboards/dash_directivo.html', {'nombre': nombre_usuario})

@login_required
def dash_estudiante(request):
    nombre_usuario = request.user.nombre
    # Aquí podrías agregar lógica para manejar la vista del dashboard del estudiante
    return render(request, 'dasboards/dash_estudiante.html', {'nombre': nombre_usuario})

@login_required
def dash_padre(request):
    nombre_usuario = request.user.nombre
    # Aquí podrías agregar lógica para manejar la vista del dashboard del padre
    return render(request, 'dasboards/dash_padre.html', {'nombre': nombre_usuario})

@login_required
def dash_docente(request):
    nombre_usuario = request.user.nombre
    # Aquí podrías agregar lógica para manejar la vista del dashboard del docente
    return render(request, 'dasboards/dash_docente.html', {'nombre': nombre_usuario})