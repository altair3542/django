# relatos/forms.py

from django import forms
from .models import Relato
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

  # Si pasa la validación, retornamos el valor limpio

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

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
