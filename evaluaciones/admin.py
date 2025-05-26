from django.contrib import admin
from .models import Nota

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'asignatura', 'nota_acumulada', 'primer_examen', 'segundo_examen', 'examen_final')
    search_fields = ('estudiante__username', 'asignatura__nombre')

from django.contrib import admin
from .models import EvaluacionDiaria

@admin.register(EvaluacionDiaria)
class EvaluacionDiariaAdmin(admin.ModelAdmin):
    list_display = ('curso', 'asignatura', 'estudiante', 'is_participate', 'is_tarea', 'is_present')
    list_filter = ('is_present',)

from django.contrib import admin
from .models import TestVak

@admin.register(TestVak)
class TestVAKAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'visual', 'auditorio', 'lectutura', 'kinestesico', 'estilo_predominante')
    search_fields = ('estudiante__username',)
