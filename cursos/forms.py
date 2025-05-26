from django import forms
from .models import Inscripcion, Curso
from usuarios.models import Usuario

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
    class Meta:
        model = Curso
        fields = ['docente', 'horario', 'dias']
        widgets = {
            'docente': forms.Select(),
            'horario': forms.TextInput(),
            'dias': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['docente'].queryset = Usuario.objects.filter(rol='docente')