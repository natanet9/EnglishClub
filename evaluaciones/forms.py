from django import forms
from .models import EvaluacionDiaria, Nota, TestVak

class EvaluacionDiariaForm(forms.ModelForm):
    class Meta:
        model = EvaluacionDiaria
        fields = ['curso', 'asignatura', 'estudiante', 'is_participate', 'is_tarea', 'is_present']
        labels = {
            'curso': 'Curso Asignado',
            'asignatura': 'Asignatura Evaluada',
            'estudiante': 'Nombre del Estudiante',
            'is_participate': 'Participación',
            'is_tarea': 'Entrega de Tarea',
            'is_present': '¿Asistió?',
        }

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['estudiante', 'asignatura', 'nota_acumulada', 'primer_examen', 'segundo_examen', 'examen_final']
        labels = {
            'estudiante': 'Nombre del Estudiante',
            'asignatura': 'Asignatura',
            'nota_acumulada': 'Nota Acumulada',
            'primer_examen': 'Primer Examen',
            'segundo_examen': 'Segundo Examen',
            'examen_final': 'Examen Final',
        }

class TestVakForm(forms.ModelForm):
    class Meta:
        model = TestVak
        fields = ['visual', 'auditorio', 'lectutura', 'kinestesico', 'estilo_predominante', 'estudiante']
        labels = {
            'visual': 'Porcentaje Visual',
            'auditorio': 'Porcentaje Auditivo',
            'lectutura': 'Porcentaje de Lectura',
            'kinestesico': 'Porcentaje Kinestésico',
            'estilo_predominante': 'Estilo Predominante',
            'estudiante': 'Nombre del Estudiante',
        }
