from django import forms
from .models import Post

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['nombre', 'contenido', 'imagen', 'categoria', 'etiqueta']
        labels = {
            'nombre': 'Nombre',
            'contenido': 'Contenido',
            'imagen': 'Imagen',
            'categoria': 'Categoria',
            'etiqueta': 'Etiqueta',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'etiqueta': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }