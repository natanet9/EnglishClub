from django.contrib import admin
from .models import PermisoAusencia

@admin.register(PermisoAusencia)
class PermisoAusenciaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'fecha', 'curso', 'asignatura', 'aprobado')
    list_filter = ('aprobado', 'fecha')
    search_fields = ('estudiante__username',)
