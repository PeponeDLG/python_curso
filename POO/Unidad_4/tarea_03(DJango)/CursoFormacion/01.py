import os
import django

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CursosFormacion.settings')
django.setup()

from cursos.models import Curso

class Main:
    @staticmethod
    def main():
        os.system("clear")

if __name__=="__main__":    
    Main.main()