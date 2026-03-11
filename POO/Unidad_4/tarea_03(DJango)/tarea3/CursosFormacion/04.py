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
        
        curso = Curso.objects.values_list('tipo').annotate(total=Count("tipo"))
        
        for c in curso:
            print(c)

if __name__=="__main__":    
    Main.main()