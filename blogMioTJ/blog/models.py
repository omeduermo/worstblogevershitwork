from django.db import models

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
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='categoria')
    etiqueta = models.ManyToManyField(Etiqueta, related_name='etiqueta')
    
    def __str__(self):
        return f"{self.nombre} - {self.fecha.strftime('%d/%m/%Y')}"
    
    class Meta:
        db_table = 'posts'
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'