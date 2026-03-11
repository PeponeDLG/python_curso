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
                
        curso = Curso.objects.filter(fecha_inicio__lte='2026-03-01',fecha_fin__gte='2026-03-01')       
        
        for c in curso:
            print(c)

if __name__=="__main__":    
    Main.main()