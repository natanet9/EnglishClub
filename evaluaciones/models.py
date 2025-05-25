from django.db import models
from usuarios.models import Usuario
from asignaturas.models import Asignatura
from cursos.models import Curso

class EvaluacionDiaria(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    is_participate = models.SmallIntegerField()
    is_tarea = models.SmallIntegerField()
    is_present = models.BooleanField()

    def __str__(self):
        return f"Evaluación de {self.estudiante} en {self.asignatura}"


class Nota(models.Model):
    estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notas')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    nota_acumulada = models.IntegerField()
    primer_examen = models.IntegerField()
    segundo_examen = models.IntegerField()
    examen_final = models.IntegerField()

    class Meta:
        db_table = "nota"

    def __str__(self):
        return f"Nota de {self.estudiante} en {self.asignatura}"


class TestVak(models.Model):
    visual = models.FloatField()
    auditorio = models.FloatField()
    lectutura = models.FloatField()
    kinestesico = models.FloatField()
    estilo_predominante = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    class Meta:
        db_table = "test_vak"

    def __str__(self):
        return f"Test VAK de {self.estudiante}"
