import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_django_orm.settings')
django.setup()

from empleados.models import Empleado

class Main:
    @staticmethod
    def main():
        pass

if __name__=="__main__":
    Main.main()