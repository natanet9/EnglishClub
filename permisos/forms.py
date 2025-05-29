from django import forms
from .models import PermisoAusencia

class PermisoAusenciaForm(forms.ModelForm):
    class Meta:
        model = PermisoAusencia
        fields = ['estudiante', 'curso', 'asignatura', 'fecha', 'motivo']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'border rounded px-3 py-2 w-full'}),
            'motivo': forms.Textarea(attrs={'class': 'border rounded px-3 py-2 w-full', 'rows': 3}),
        }
        labels = {
            'motivo': 'Motivo de la ausencia',
            'fecha': 'Fecha de la ausencia',
        }
