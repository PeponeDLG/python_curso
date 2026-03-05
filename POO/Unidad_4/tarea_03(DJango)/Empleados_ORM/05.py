import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Empleados_ORM.settings')
django.setup()

from empleados.models import Empleado

class Main:
    @staticmethod
    def main():
        os.system("clear")
        
        empleados = Empleado.objects.all().order_by('-apellidos', '-nombre')
        
        [print(empleado.__str__()) for empleado in empleados]

if __name__=="__main__":
    Main.main()