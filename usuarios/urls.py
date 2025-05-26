# usuarios/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_view, crear_estudiante_tecnico

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('crear/tecnico/', crear_estudiante_tecnico, name='crear_estudiante_tecnico'),
    #path('crear/regular/', crear_estudiante_regular, name='crear_estudiante_regular'),
    #path('crear/tutor/', crear_tutor, name='crear_tutor'),

    #path('registrado/', estudiante_registrado, name='estudiante_registrado'),
    #path('registrado/tutor/', estudiante_tutor_registrado, name='estudiante_tutor_registrado'),
]
