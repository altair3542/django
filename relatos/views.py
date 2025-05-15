from django.shortcuts import render
from .models import Relato
# Create your views here.

def home(request):
    contexto = {
        'titulo': 'Blog de salidas',
        'mensaje': '¡Comparte aquí tus chocoaventuras configurando el proyecto.!'
    }
    return render(request, 'home.html', contexto)


def acerca(request):
    contexto = {
        'titulo': 'Acerca de mí',
        'nombre': 'Santiago',
        'bio': 'Soy tu profesor de programación, apasionado por Django y la POO. Aquí compartiré con ustedes mis experiencias y trucos.'
    }
    return render(request, 'acerca.html', contexto)

def lista_relatos(request):
    relatos = Relato.objects.all()  
    contexto = {
        'relatos': relatos,
        'titulo': 'Listado de Relatos'
    }
    return render(request, 'relatos/lista_relatos.html', contexto)
