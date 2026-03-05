import os
import django
from django.db.models import Avg, Count, Max, Min

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Empleados_ORM.settings')
django.setup()

from empleados.models import Empleado

class Main:
    @staticmethod
    def main():
        os.system("clear")
        max = Empleado.objects.aggregate(Max('salario'))
        min = Empleado.objects.aggregate(Min('salario'))
        conteo = Empleado.objects.filter(departamento='ventas').aggregate(Count('id'))
        # media = Empleado.objects.filter(departamento='ventas').aggregate(Avg('salario'))
        media = Empleado.objects.aggregate(Avg('salario'))
        
        print(f"Salario máximo:{max['salario__max']}")
        print(f"Salario mínimo:{min['salario__min']}")
        print(f"Media salios:{round(media['salario__avg'],ndigits=2)}")
        print(f"Nº empleados en ventas:{conteo['id__count']}")

if __name__=="__main__":
    Main.main()