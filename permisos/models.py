from django.db import models
from usuarios.models import Usuario
from cursos.models import Curso
from asignaturas.models import Asignatura

class PermisoAusencia(models.Model):
    estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField()
    motivo = models.TextField()
    aprobado = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)

    class Meta:
        db_table = 'permiso_ausencia'
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.estudiante} - {self.fecha} - {'Aprobado' if self.aprobado else 'Pendiente'}"
