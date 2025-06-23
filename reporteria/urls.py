# reportes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_reportes, name='vista_reportes'),

    path('exportar/pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('exportar/excel/', views.exportar_excel, name='exportar_excel'),
]
