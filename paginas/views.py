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



def dash_directivo(request):
    # Aquí podrías agregar lógica para manejar la vista del dashboard del docente/directivo
    return render(request, 'dasboards/dash_directivo.html')

def dash_estudiante(request):
    # Aquí podrías agregar lógica para manejar la vista del dashboard del estudiante
    return render(request, 'dasboards/dash_estudiante.html')

def dash_padre(request):
    # Aquí podrías agregar lógica para manejar la vista del dashboard del padre
    return render(request, 'dasboards/dash_padre.html')

def dash_docente(request):
    # Aquí podrías agregar lógica para manejar la vista del dashboard del docente
    return render(request, 'dasboards/dash_docente.html')