from django.db import models

# Create your models here.
class Tarea(models.Model):
  titulo = models.CharField(max_length = 256, default = "---")
  # Estado: 0, indica tarea pendiente
  # Estado: 1, indica tarea compleada
  estado = models.BooleanField(default = 0)
  