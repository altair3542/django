from django.db import models

# Create your models here.
# generaremos 2 modelos... autor: va a escribir los relatos
# Relato: una historia de viaje escrita por un autor...

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.nombre)

class Relato(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='relatos')

    def __str__(self):
        return f"{self.titulo} ({self.autor.nombre})"


# Explicación:
# CharField y TextField: campos de texto.

# DateField(auto_now_add=True): guarda la fecha cuando se crea el relato.

# ForeignKey: relación uno-a-muchos (1 autor → muchos relatos).

# on_delete=models.CASCADE: si se elimina el autor, se eliminan sus relatos.

# related_name='relatos': permite usar autor.relatos.all() para obtener sus relatos.
