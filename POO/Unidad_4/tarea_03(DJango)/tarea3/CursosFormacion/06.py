import os
import django
from django.db.models import Avg, Count, Max, Min

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CursosFormacion.settings')
django.setup()

from curso.models import Curso

class Main:
    @staticmethod
    def main():
        os.system("clear")
        
        min_horas = 2
        max_horas = 4
        
        curso = Curso.objects.filter(horas__range=(min_horas, max_horas))
        
        for c in curso:
            print(c)

if __name__=="__main__":    
    Main.main()