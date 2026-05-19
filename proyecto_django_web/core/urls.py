from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('inicio/', views.inicio, name='inicio'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('alertas/', views.alertas, name='alertas'),
    path('importar/', views.importar, name='importar'),
    path('acerca/', views.acerca, name='acerca'),
]
