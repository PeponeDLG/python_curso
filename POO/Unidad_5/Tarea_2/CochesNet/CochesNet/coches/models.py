from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        db_table = "Marca"


class Coche(models.Model):
    marca = models.ForeignKey(to="Marca", on_delete=models.RESTRICT)
    modelo = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    potencia = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    fecha_fabricacion = models.DateField()

    def __str__(self):
        return f"{self.modelo}"
    
    class Meta:
        db_table = "Coche"

