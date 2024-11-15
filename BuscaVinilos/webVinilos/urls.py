# webVinilos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página principal
    path('buscar/', views.buscar, name='buscar'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('gestor/', views.gestor, name='gestor'),
    path('filtrar-artistas/', views.filtrar_artistas, name='filtrar_artistas'),
]
