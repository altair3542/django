from django.shortcuts import render

# Create your views here.

def home(request):
    contexto = {
        'titulo': 'Blog de salidas',
        'mensaje': '¡Comparte aquí tus chocoaventuras en el lleras.!'
    }
    return render(request, 'home.html', contexto)


def acerca(request):
    contexto = {
        'titulo': 'Acerca de mí',
        'nombre': 'Santiago',
        'bio': 'Soy tu profesor de programación, apasionado por Django y la POO. Aquí compartiré con ustedes mis experiencias y trucos.'
    }
    return render(request, 'acerca.html', contexto)
