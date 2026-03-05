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
        empleados = [
            Empleado(nombre = "pepe",apellidos = "prueba",salario = "1000",departamento = "ventas"),
            Empleado(nombre = "pepe2",apellidos = "prueba2",salario = "1002",departamento = "ventas"),
            Empleado(nombre = "pepe3",apellidos = "prueba3",salario = "1003",departamento = "ventas"),
            Empleado(nombre = "juan",apellidos = "solomillo",salario = "900",departamento = "marketing"),
            Empleado(nombre = "jesús",apellidos = "garcía",salario = "1200",departamento = "conserjería"),
            Empleado(nombre = "Chavo",apellidos = "prueba4",salario = "1004",departamento = "ventas")
            ]
        
        for i in empleados:
            i.save()
            print(f"Empleado: {i.nombre} guardado en BBDD")
        

if __name__=="__main__":    
    Main.main()