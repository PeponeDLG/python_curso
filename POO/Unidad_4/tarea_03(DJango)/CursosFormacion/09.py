import os
import django
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Configuración del entorno Django (ajusta con tu proyecto)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CursosFormacion.settings')
django.setup()

from curso.models import Curso

class Main:
    @staticmethod
    def main():
        os.system("clear")
                
        curso = Curso.objects.filter(fecha_inicio__gt='2026-03-01')       
        
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_pdf = os.path.join(directorio_actual, "cursos_proximos.pdf")
        doc = SimpleDocTemplate(ruta_pdf, pagesize=letter)
        
        contenido = []
        
        for c in curso:
            parrafo = Paragraph(c.__str__())
            contenido.append(parrafo)
            
        doc.build(contenido)

if __name__=="__main__":    
    Main.main()