from django import forms
from .models import Inscripcion, Curso
from usuarios.models import Usuario
import json
import re

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso', 'nivel', 'secretaria', 'fecha_inscripcion']
        widgets = {
            'fecha_inscripcion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'estudiante': forms.Select(),
            'curso': forms.Select(),
            'secretaria': forms.Select(),
            'nivel': forms.Select(choices=[
                ('Basico', 'Básico'),
                ('Intermedio', 'Intermedio'),
                ('Avanzado', 'Avanzado'),
            ]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['estudiante'].queryset = Usuario.objects.filter(rol='estudiante')
        self.fields['secretaria'].queryset = Usuario.objects.filter(rol='secretaria')
        self.fields['curso'].queryset = Curso.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        estudiante = cleaned_data.get('estudiante')
        curso = cleaned_data.get('curso')
        if estudiante and curso:
            if Inscripcion.objects.filter(estudiante=estudiante, curso=curso).exists():
                raise forms.ValidationError('El estudiante ya está inscrito en este curso.')
        return cleaned_data

class CursoForm(forms.ModelForm):
    DIAS_SEMANA = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    dias = forms.MultipleChoiceField(
        choices=DIAS_SEMANA,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Días'
    )

    class Meta:
        model = Curso
        fields = ['docente', 'horario', 'dias']
        widgets = {
            'docente': forms.Select(attrs={'class': 'form-select'}),
            'horario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 09:00 - 12:00'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['docente'].queryset = Usuario.objects.filter(rol='docente')
       
        if self.instance and self.instance.pk and self.instance.dias:
            try:
               
                if isinstance(self.instance.dias, list):
                    self.fields['dias'].initial = self.instance.dias
                else:
                    self.fields['dias'].initial = json.loads(self.instance.dias)
            except (ValueError, TypeError):
                self.fields['dias'].initial = []

    def clean_horario(self):
        horario = self.cleaned_data.get('horario')
        if horario:
            
            pattern = r'^\d{1,2}:\d{2}\s*-\s*\d{1,2}:\d{2}$'
            if not re.match(pattern, horario):
                raise forms.ValidationError('El horario debe tener el formato HH:MM - HH:MM (ej: 09:00 - 12:00).')
        return horario

    def clean_dias(self):
        dias = self.cleaned_data.get('dias')
        if not dias:
            raise forms.ValidationError('Debe seleccionar al menos un día.')
        return dias

    def clean_docente(self):
        docente = self.cleaned_data.get('docente')
        if not docente:
            raise forms.ValidationError('Debe seleccionar un docente.')
        return docente

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.dias = self.cleaned_data['dias']
        if commit:
            instance.save()
        return instance