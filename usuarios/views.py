from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.POST.get('user-type')  # este campo debe estar en el formulario

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user_type == 'docente':
                return redirect('docente_dashboard')
            elif user_type == 'estudiante':
                return redirect('estudiante_dashboard')
            elif user_type == 'padre':
                return redirect('padre_dashboard')
            elif user_type == 'directivo':
                return redirect('directivo_dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'usuarios/login.html')
