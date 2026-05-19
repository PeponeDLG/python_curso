from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return '/inicio/'


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def inicio(request):
    return render(request, 'inicio.html', {'titulo': 'Inicio'})


@login_required
def dashboard(request):
    metricas = [
        {'titulo': 'Total de registros', 'valor': '1,500', 'icono': '📊'},
        {'titulo': 'Alertas activas', 'valor': '3', 'icono': '⚠️'},
        {'titulo': 'Usuarios registrados', 'valor': '2', 'icono': '👥'},
        {'titulo': 'Tareas completadas', 'valor': '87%', 'icono': '✅'},
    ]
    return render(request, 'dashboard.html', {'titulo': 'Dashboard', 'metricas': metricas})


@login_required
def alertas(request):
    alertas_lista = [
        {'id': 1, 'tipo': 'Crítica', 'mensaje': 'Fallo en el servidor de base de datos', 'fecha': '2026-05-18', 'estado': 'Activa'},
        {'id': 2, 'tipo': 'Alta', 'mensaje': 'Uso de CPU superior al 90%', 'fecha': '2026-05-18', 'estado': 'Activa'},
        {'id': 3, 'tipo': 'Media', 'mensaje': 'Espacio en disco por debajo del 20%', 'fecha': '2026-05-17', 'estado': 'Pendiente'},
        {'id': 4, 'tipo': 'Baja', 'mensaje': 'Actualización de seguridad disponible', 'fecha': '2026-05-17', 'estado': 'Pendiente'},
        {'id': 5, 'tipo': 'Crítica', 'mensaje': 'Intento de acceso no autorizado', 'fecha': '2026-05-16', 'estado': 'Resuelta'},
        {'id': 6, 'tipo': 'Media', 'mensaje': 'Certificado SSL próximo a expirar', 'fecha': '2026-05-16', 'estado': 'Resuelta'},
        {'id': 7, 'tipo': 'Alta', 'mensaje': 'Servicio de correo fuera de línea', 'fecha': '2026-05-15', 'estado': 'Resuelta'},
        {'id': 8, 'tipo': 'Baja', 'mensaje': 'Versión de Python desactualizada', 'fecha': '2026-05-15', 'estado': 'Resuelta'},
        {'id': 9, 'tipo': 'Media', 'mensaje': 'Latencia alta en API externa', 'fecha': '2026-05-14', 'estado': 'Resuelta'},
    ]
    return render(request, 'alertas.html', {'titulo': 'Alertas', 'alertas': alertas_lista})


@login_required
def importar(request):
    return render(request, 'importar.html', {'titulo': 'Importación de datos'})


@login_required
def acerca(request):
    return render(request, 'acerca.html', {'titulo': 'Acerca del proyecto'})
