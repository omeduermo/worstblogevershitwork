from django.contrib import admin
from .models import Categoria, Post, Etiqueta

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'imagen')
    search_fields = ('nombre',)
    list_filter = ('categoria', 'etiqueta')
    ordering = ('fecha',)

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ('nombre', 'slug')
    search_fields = ('nombre',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}
    list_display = ('nombre', 'slug')
    search_fields = ('nombre',)