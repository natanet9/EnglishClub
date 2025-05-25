from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from apps.usuarios.models import Usuario
from apps.directivos.models import Directivo  # Asegúrate de importar el modelo correcto


def login_view(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('username', '').strip()
        contrasena = request.POST.get('password', '')
        rol = request.POST.get('user-type', '')

        try:
            usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)

            if not usuario.activo:
                messages.error(request, 'El usuario está inactivo.')
                return render(request, 'usuarios/login.html')

            if not check_password(contrasena, usuario.contrasena):
                messages.error(request, 'Contraseña incorrecta.')
                return render(request, 'usuarios/login.html')

            if usuario.rol != rol:
                messages.error(request, 'Rol incorrecto. Seleccione el rol adecuado.')
                return render(request, 'usuarios/login.html')

            # Autenticación exitosa
            request.session['id_usuario'] = usuario.id
            request.session['nombre_usuario'] = usuario.nombre_usuario
            request.session['rol'] = usuario.rol

            # Redirección por rol
            redirecciones = {
                'directivo': 'dashboard_directivo',
                'estudiante': 'dashboard_estudiante',
                'tutor': 'dashboard_tutor',  # por si luego lo agregas
            }

            return redirect(redirecciones.get(rol, 'inicio'))

        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')

    return render(request, 'usuarios/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('inicio')

def dashboard_directivo(request):
    if request.session.get('rol') != 'directivo':
        return redirect('login')
    
    nombre = request.session.get('nombre_usuario', 'Directivo')
    return render(request, 'directivos/dashboard_directivo.html', {'nombre': nombre})
def dashboard_directivo(request):
    if request.session.get('rol') != 'directivo':
        return redirect('login')

    id_usuario = request.session.get('id_usuario')

    try:
        directivo = Directivo.objects.get(usuario_id=id_usuario)
        nombre = f"{directivo.nombres} {directivo.apellidos}"
    except Directivo.DoesNotExist:
        nombre = 'Directivo'

    return render(request, 'directivos/dashboard_directivo.html', {'nombre': nombre})

def agregar_usuario(request):
    if request.method == 'POST':
        nombre_usuario = request.POST.get('nombre_usuario', '').strip()
        contrasena = request.POST.get('contrasena', '')
        rol = request.POST.get('rol', '').strip()
        ref_id = request.POST.get('ref_id')
        activo = request.POST.get('activo') == 'on'

        if not nombre_usuario or not contrasena or not rol:
            messages.error(request, 'Por favor, completa todos los campos obligatorios.')
            return render(request, 'usuarios/agregar_usuario.html')

        if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return render(request, 'usuarios/agregar_usuario.html')

        hashed_pass = make_password(contrasena)
        usuario = Usuario(
            nombre_usuario=nombre_usuario,
            contrasena=hashed_pass,
            rol=rol,
            ref_id=ref_id if ref_id else None,
            activo=activo
        )
        usuario.save()
        messages.success(request, f'Usuario "{nombre_usuario}" creado con éxito.')
        return redirect('login')  # Cambia a donde quieras redirigir después

    return render(request, 'usuarios/agregar_usuario.html')