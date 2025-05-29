from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Usuario
from .forms import EstudianteRegularForm, EstudianteTecnicoForm, TutorForm
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('usuarios:login')
      
def login_view(request):
    if request.user.is_authenticated:
        user_type = getattr(request.user, 'rol', None)
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user-type')
        user = authenticate(request, username=username, password=password)  
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'usuarios/login.html')   

def is_secretaria_or_directivo(user):
    return user.is_authenticated and user.rol in ['secretaria', 'directivo']

@login_required
@user_passes_test(is_secretaria_or_directivo)
def crear_estudiante_regular(request):
    print("Vista de registro llamada. Método:", request.method)
    form = EstudianteRegularForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            try:
                usuario = Usuario.objects.create_user(
                    carnet=data['carnet'],
                    nombre=data['nombre'],
                    apellidos=data['apellidos'],
                    contraseña=data['password'],
                    username=data['username'],
                    direccion=data['direccion'],
                    telefono=data['telefono'],
                    fecha_nacimiento=data['fecha_nacimiento'],
                    domicilio=data['domicilio'],
                    rol='estudiante',
                )
                messages.success(request, "✅ Estudiante regular creado exitosamente.")
                return redirect('usuarios:asignar_tutor', estudiante_id=usuario.id)
            except Exception as e:
                messages.error(request, f"❌ Error al guardar estudiante: {str(e)}")
        else:
            print(form.errors)
            messages.error(request, "❌ Formulario inválido. Revisa los campos.")
    return render(request, 'Registros/estudiante_regular.html', {
        'form': form,
        'today': now().date(),
        'dias_semana': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
    })

@login_required
@user_passes_test(is_secretaria_or_directivo)
def crear_estudiante_tecnico(request):
    form = EstudianteTecnicoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            try:
                usuario = Usuario.objects.create_user(
                    username=data['username'],
                    carnet=data['carnet'],
                    nombre=data['nombre'],
                    apellidos=data['apellidos'],
                    contraseña=data['password'],
                    direccion=data['direccion'],
                    telefono=data['telefono'],
                    fecha_nacimiento=data['fecha_nacimiento'],
                    domicilio=data['domicilio'],
                    rol='estudiante',
                    ocupacion=data.get('ocupacion', ''),
                )
                messages.success(request, "✅ Estudiante técnico creado exitosamente.")
                return redirect('usuarios:estudiante_registrado')
            except Exception as e:
                messages.error(request, f"❌ Error al guardar estudiante: {str(e)}")
        else:
            messages.error(request, "❌ Formulario inválido. Revisa los campos.")
    return render(request, 'Registros/estudiante_tecnico.html', {
        'form': form,
        'today': now().date(),
        'dias_semana': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
    })

@login_required
@user_passes_test(is_secretaria_or_directivo)
def asignar_tutor(request, estudiante_id):
    try:
        estudiante = Usuario.objects.get(id=estudiante_id)
    except Usuario.DoesNotExist:
        messages.error(request, "❌ Estudiante no encontrado.")
        return redirect('usuarios:crear_estudiante_regular')
    usuarios = Usuario.objects.filter(rol='padre')
    tutor_form = TutorForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        action = request.POST.get('action')
        print("Acción recibida:", action)  # Para depuración
        if action == 'select_tutor':
            tutor_id = request.POST.get('tutor_id')
            if tutor_id:
                try:
                    tutor = Usuario.objects.get(id=tutor_id)
                    hijo_dict = tutor.hijo if isinstance(tutor.hijo, dict) else {}
                    hijo_dict[estudiante.carnet] = {'id': estudiante.id}
                    tutor.hijo = hijo_dict
                    tutor.save()
                    messages.success(request, "✅ Tutor asignado exitosamente.")
                    return redirect('usuarios:estudiante_registrado')
                except Exception as e:
                    messages.error(request, f"❌ Error al asignar tutor: {str(e)}")
        elif action == 'create_tutor' and tutor_form.is_valid():
            data = tutor_form.cleaned_data
            try:
                tutor = Usuario.objects.create_user(
                    username=data['username'],
                    carnet=data['carnet'],
                    nombre=data['nombre'],
                    apellidos=data['apellidos'],
                    contraseña=data['password'],
                    direccion=data['direccion'],
                    telefono=data['telefono'],
                    fecha_nacimiento=data['fecha_nacimiento'],
                    domicilio=data['domicilio'],
                    rol='padre',
                    ocupacion=data.get('ocupacion', ''),
                    hijo={estudiante.carnet: {'id': estudiante.id}}
                )
                messages.success(request, "✅ Tutor creado y asignado exitosamente.")
                return redirect('usuarios:estudiante_registrado')
            except Exception as e:
                messages.error(request, f"❌ Error al crear tutor: {str(e)}")
        else:
            print("Errores del formulario:", tutor_form.errors)
            messages.error(request, "❌ Formulario inválido. Revisa los campos.")
    return render(request, 'Registros/asignar_tutor.html', {
        'estudiante': estudiante,
        'usuarios': usuarios,
        'tutor_form': tutor_form
    })
    
def estudiante_registrado(request):
    return render(request, 'Registros/estudiante_registrado.html')