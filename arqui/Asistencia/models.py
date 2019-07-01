from django.db import models
from django.utils import timezone
from Alumno.models import Alumno

class Asistencia(models.Model):
    idAlumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    fecha=models.DateTimeField(default=timezone.now)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fecha

    class Meta:
        db_table = 'Asistencia'

# Create your models here.
