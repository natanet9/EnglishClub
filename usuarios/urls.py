# usuarios/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_view,logout_view, crear_estudiante_regular, crear_estudiante_tecnico, asignar_tutor, estudiante_registrado

app_name = 'usuarios'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('crear/regular/', crear_estudiante_regular, name='crear_estudiante_regular'),
    path('crear/tecnico/', crear_estudiante_tecnico, name='crear_estudiante_tecnico'),
    path('registrado/', estudiante_registrado, name='estudiante_registrado'),
    path('asignar-tutor/<int:estudiante_id>/', asignar_tutor, name='asignar_tutor'),

    #path('registrado/', estudiante_registrado, name='estudiante_registrado'),
    #path('registrado/tutor/', estudiante_tutor_registrado, name='estudiante_tutor_registrado'),
]
