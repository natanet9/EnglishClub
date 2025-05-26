from django.contrib import admin
from .models import Inscripcion

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_inscripcion', 'nivel', 'estudiante', 'secretaria', 'curso')
    list_filter = ('nivel',)
    search_fields = ('estudiante__username', 'curso__id')

from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'docente', 'horario')
    search_fields = ('docente__username',)
