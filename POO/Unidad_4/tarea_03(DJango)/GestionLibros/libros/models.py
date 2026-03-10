from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100, blank=True, null=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)    
    editorial = models.CharField(max_length=100, blank=False, null=False)
    fecha_lanzamiento = models.DateField()
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        db_table = "libros"

