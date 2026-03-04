from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    departamento = models.TextField(max_length=50, blank=True, null=True)
    fecha_contratacion = models.DateField(null=True, blank=True, auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.salario} - {self.departamento} - {self.fecha_contratacion}"