# Aqui importamos las librerias y los modelos
from django.shortcuts import render, redirect, get_object_or_404
from .models import Relato, Autor
from .forms import AutorForm, RelatoForm

# Create your views here.


# creamos una funcion de vista que renderice en el home de la pagina web
def home(request):
    contexto = {
        'titulo': 'Blog de salidas',
        'mensaje': '¡Comparte aquí tus chocoaventuras configurando el proyecto.!'
    }
    return render(request, 'home.html', contexto)

# creamos una funcion de vista que renderice en la pagina "acerca" de la pagina web
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

def agregar_autor(request):
    # Vista para mostrar y procesar el formulario de
    # creacion de autores.
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()

    return render(request, 'relatos/agregar_autor.html', {'form': form, 'titulo': 'Agregar Autor' })

def agregar_relato(request):
    if request.method == 'POST':
        form = RelatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_relatos')
    else:
        form = RelatoForm

    return render(request, 'relatos/agregar_relato.html', {'form': form, 'titulo': 'Agregar Relato'})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'relatos/lista_autores.html', {'autores': autores, 'titulo': 'Listado de autores' })

def detalle_relato(request, relato_id):
    relato = get_object_or_404(Relato, id=relato_id)
    return render(request, 'relatos/detalle_relato.html', {'relato': relato})
