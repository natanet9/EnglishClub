from django.shortcuts import render

# Vista para la página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista para la página ¿Quiénes Somos?
def quienes_somos(request):
    return render(request, 'quienes_somos.html')

# Vista para la página de Servicios
def servicios(request):
    return render(request, 'servicios.html')

# Vista para la página de Contacto
def contacto(request):
    return render(request, 'contacto.html')