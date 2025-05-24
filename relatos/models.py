from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# generaremos 2 modelos... autor: va a escribir los relatos
# Relato: una historia de viaje escrita por un autor...


class Relato(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='relatos')

    def __str__(self):
        return f"{self.titulo} ({self.autor.username})"


# Explicación:
# CharField y TextField: campos de texto.

# DateField(auto_now_add=True): guarda la fecha cuando se crea el relato.

# ForeignKey: relación uno-a-muchos (1 autor → muchos relatos).

# on_delete=models.CASCADE: si se elimina el autor, se eliminan sus relatos.

# related_name='relatos': permite usar autor.relatos.all() para obtener sus relatos.
