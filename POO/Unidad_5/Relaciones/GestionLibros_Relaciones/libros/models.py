from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_lanzamiento = models.DateField()
    editorial = models.ForeignKey(to='Editorial', on_delete=models.RESTRICT)

    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = 'libros'

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}- {self.pais}'
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    libros = models.ManyToManyField(to='Libro')

    def __str__(self):
        return f"{self.nombre} - {self.pais}"

class DatosContacto(models.Model):
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    autor = models.OneToOneField(to='Autor', on_delete=models.RESTRICT)

    def __str__(self):
        return f"{self.email} - {self.telefono}"
