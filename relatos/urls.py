from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca/', views.acerca, name='acerca'),
    path('relatos/', views.lista_relatos, name='lista_relatos'),
    path('relatos/agregar/', views.agregar_relato, name='agregar_relato'),
    path('relatos/<int:relato_id>/', views.detalle_relato, name='detalle_relato'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/agregar/', views.agregar_autor, name='agregar_autor' ),
]
