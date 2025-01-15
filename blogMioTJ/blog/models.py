from django.db import models

class post(models.Model):
    nombre = models.CharField("Nombre", max_length=50)
    contenido = models.TextField("Contenido")
    fecha = models.DateTimeField("Fecha", auto_now_add=True)
    imagen = models.ImageField(
        "Imagen", upload_to="posts", null=True, blank=True
    )
    
    def __str__(self):
        return f"{self.nombre} - {self.fecha.strftime('%d/%m/%Y')}"
    
    class Meta:
        db_table = 'Posts'
        managed = True
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'