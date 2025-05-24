# Aqui importamos las librerias y los modelos
from django.shortcuts import render, redirect, get_object_or_404
from .models import Relato
from .forms import RelatoForm, RegistroUsuarioForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


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

@login_required
def agregar_relato(request):
    if request.method == 'POST':
        form = RelatoForm(request.POST)
        if form.is_valid():
            relato = form.save(commit=False)
            relato.autor = request.user
            relato.save()
            return redirect('lista_relatos')
    else:
        form = RelatoForm

    return render(request, 'relatos/agregar_relato.html', {'form': form, 'titulo': 'Agregar Relato'})



def detalle_relato(request, relato_id):
    relato = get_object_or_404(Relato, id=relato_id)
    return render(request, 'relatos/detalle_relato.html', {'relato': relato})

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request,usuario)
            return redirect('lista_relatos')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'relatos/registro.html', {'form' : form})
