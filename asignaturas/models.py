from django.db import models

class Asignatura(models.Model):
    nombre = models.CharField(max_length=255)
    nivel = models.CharField(max_length=100)

    class Meta:
        db_table = "asignatura"

    def __str__(self):
        return f"{self.nombre} ({self.nivel})"

