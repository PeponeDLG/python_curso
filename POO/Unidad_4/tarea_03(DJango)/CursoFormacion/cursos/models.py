from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    horas = models.IntegerField()
    tipo = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Curso: {self.nombre} - descripción: {self.descripcion} - horas: {self.horas} - tipo: {self.tipo} - " \
            f"fecha inicio: {self.fecha_inicio} - fecha fin: {self.fecha_fin} - precio: {self.precio}"
            
    class Meta:
        db_table = "cursos"
