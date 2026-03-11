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
        ids = Empleado.objects.all()
        
        print("IDs disponibles: ")
        [print(i.id,", ", end="") for i in ids]
        
        id_ = input("Introduzca una ID existente:")
        
        empleado = Empleado.objects.get(id=id_)
        print(f"Ha escogido al empleado:\n{empleado.__str__()}")
        
        empleado.salario = input("Introduzca el nuevo salario: ")
        
        empleado.save()
        empleado = Empleado.objects.get(id=id_)
                
        print(f"El empleado con ID \"{id_}\" ha sido actualizado:\n{empleado.__str__()}")

if __name__=="__main__":
    Main.main()