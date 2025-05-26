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
    return render(request, 'dasboards/dash_docente.html')