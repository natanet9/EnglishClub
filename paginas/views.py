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
def dashboard(request):
    usuario = request.user  # O request.user.username si no usas first_name
    return render(request, 'dasboards/dashboard.html', {'usuario': usuario})