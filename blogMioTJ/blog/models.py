from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField("Nombre", max_length=50, unique=True)
    slug = models.SlugField("Slug", max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'categoria'
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']
        
class Etiqueta(models.Model):
    nombre = models.CharField("nombre", max_length=50, unique=True)
    slug = models.SlugField("Slug", max_length=50, unique=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'etiqueta'
        managed = True
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['nombre']

class Post(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    contenido = models.TextField("Contenido")
    fecha = models.DateTimeField("Fecha", auto_now_add=True)
    imagen = models.ImageField(
        "Imagen", upload_to="posts", null=True, blank=True
    )
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='posts')
    etiqueta = models.ManyToManyField(Etiqueta, related_name='posts_etiqueta')
    
    def __str__(self):
        return f"{self.nombre} - {self.fecha.strftime('%d/%m/%Y')}"
    
    class Meta:
        db_table = 'posts'
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
class Comentario (models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=255)
    content = models.TextField("Contenido")
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comentario de {self.autor} en {self.post.nombre}'
    
    class meta:
        db_table = 'comentario'
        managed= True
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'