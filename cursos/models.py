from django.db import models
from usuarios.models import Usuario

class Curso(models.Model):
    docente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='cursos')
    horario = models.CharField(max_length=255)
    dias = models.JSONField()

    class Meta:
        db_table = "curso"

    def __str__(self):
        return f"Curso {self.id} - Docente: {self.docente}"


class Inscripcion(models.Model):
    fecha_inscripcion = models.DateTimeField()
    nivel = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripciones_como_estudiante')
    secretaria = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='inscripciones_como_secretaria')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        db_table = "inscripcion"

    def __str__(self):
        return f"Inscripción de {self.estudiante} a curso {self.curso}"
