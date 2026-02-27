from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=15, null=True)
    correo = models.CharField(null=True)

    def __str__(self):
        return f"{self.nombre} - {self.telefono} - {self.correo}"