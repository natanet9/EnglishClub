from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user-type')  # este campo debe estar en el formulario

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'usuarios/login.html')


def crear_estudiante_tecnico(request):
    form = UsuarioForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        archivo = request.FILES.get('archivo_formulario')
        archivo_path = ''
        if archivo:
            archivo_path = f"formularios/{archivo.name}"
            with open(f"media/{archivo_path}", 'wb+') as destination:
                for chunk in archivo.chunks():
                    destination.write(chunk)
        try:
            # Crear el usuario con los datos del formulario
            usuario = Usuario.objects.create_user(
                carnet=data.get('carnet'),
                nombre=data.get('nombre'),
                apellidos=data.get('apellidos'),
                contraseña=data.get('password'),
                username=data.get('username'),
                direccion=data.get('direccion'),
                telefono=data.get('telefono'),
                fecha_nacimiento=data.get('fecha_nacimiento'),
                hijo=data.get('hijo'),
                domicilio=data.get('domicilio'),
                rol='estudiante',  # Rol específico
                ocupacion=data.get('ocupacion'),
            )
            usuario.save()

            messages.success(request, "✅ Estudiante técnico creado exitosamente.")
            return redirect('estudiante_registrado')
        except Exception as e:
            messages.error(request, f"❌ Error al guardar estudiante: {e}")
            return redirect('crear_estudiante_tecnico')

    return render(request, 'Registros/estudiante_tecnico.html', {
        'form': form,
        'today': now().date()
    })