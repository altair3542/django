# relatos/forms.py

from django import forms
from .models import Autor, Relato

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor  # Asociamos este formulario al modelo Autor
        fields = ['nombre', 'email']  # Campos que se mostrarán en el formulario
        labels = {
            'nombre': 'Nombre completo',
            'email': 'Correo electrónico',
        }

    def clean_nombre(self):
        """
        Validación personalizada para el campo 'nombre'.
        Se asegura que el nombre tenga al menos 5 caracteres.
        """
        nombre = self.cleaned_data.get('nombre', '')  # Obtenemos el valor enviado
        if len(nombre) < 5:
            raise forms.ValidationError("El nombre debe tener al menos 5 caracteres.")
        return nombre  # Si pasa la validación, retornamos el valor limpio

class RelatoForm(forms.ModelForm):
    class Meta:
        model = Relato  # Asociamos con el modelo Relato
        fields = ['titulo', 'contenido', 'autor']  # Campos para el formulario
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4}),  # Más espacio para contenido largo
        }
        labels = {
            'titulo': 'Título del relato',
            'contenido': 'Contenido',
            'autor': 'Autor',
        }

    def clean_titulo(self):
        """
        Validación personalizada para el campo 'titulo'.
        El título debe tener al menos 10 caracteres para asegurar calidad.
        """
        titulo = self.cleaned_data.get('titulo', '')
        if len(titulo) < 10:
            raise forms.ValidationError("El título debe tener al menos 10 caracteres.")
        return titulo
