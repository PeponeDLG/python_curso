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
                
        curso = Curso.objects.filter(tipo='tipo 4')
        
        for c in curso:
            c.precio = c.precio + 50
            c.save()
        
        for c in curso:
            print(c)

if __name__=="__main__":    
    Main.main()