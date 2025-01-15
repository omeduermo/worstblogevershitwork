from django import forms
from .models import post

class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['nombre', 'contenido', 'imagen']
        labels = {
            'nombre': 'Nombre',
            'contenido': 'Contenido',
            'imagen': 'Imagen',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
        }