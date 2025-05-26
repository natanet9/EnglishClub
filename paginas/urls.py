from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),

    path('dash-docente/', views.dash_docente, name='docente_dashboard'),
    path('dash-estudiante/', views.dash_estudiante, name='estudiante_dashboard'),
    path('dash-padre/', views.dash_padre, name='padre_dashboard'),
    path('dash-directivo/', views.dash_directivo, name='directivo_dashboard'),

]