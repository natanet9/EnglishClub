from django import forms
from .models import Asignatura

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'nivel']
        labels = {
            'nombre': 'Nombre de la Asignatura',
            'nivel': 'Nivel Académico',
        }
