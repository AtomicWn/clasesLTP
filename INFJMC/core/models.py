from django.db import models

class Carrera(models.Model):
    codigo = models.CharField(max_length=6)
    nombre = models.CharField(max_length=255)
    duracion = models.IntegerField()

