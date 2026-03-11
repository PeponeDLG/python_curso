import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CursosFormacion.settings')
django.setup()

from curso.models import Curso

class Main:
    @staticmethod
    def main():
        os.system("clear")
        
        curso = Curso.objects.all()
        
        for c in curso:
            print(c.tipo)

if __name__=="__main__":    
    Main.main()