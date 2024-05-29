from django.db import models
#from django.utils import timezone
from ckeditor.fields import RichTextField

#Importar de Modelos
from Mascota.models import Mascota

# Create your models here.

#tabla categoria
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_cat = models.CharField(max_length=50, verbose_name="Nombre de categoría")

    def __str__(self):
        return f"{self.nombre_cat}"

#tabla Blog
class Blog(models.Model):
    id_blog = models.AutoField(primary_key=True)
    foto_blog =  models.ImageField(upload_to="blog/", verbose_name="Imagen", null=True, blank=True)
    titulo_blog = models.CharField(max_length=100, verbose_name="Título")
    contenido_blog = RichTextField(verbose_name="Contenido")
    creado_blog = models.DateField(auto_now_add=True)
    #llaves foraneas
    #un blog puede tener una o muchas categorias
    categoria_blog = models.ForeignKey(Categoria, verbose_name="Categoría", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo_blog}"

#tabla Publicar Mascota
class Publicar_Mas(models.Model):
    id_pubm =models.AutoField(primary_key=True)
    fecha_pubm = models.DateField(auto_now_add=True)
    descripcion_pubm = RichTextField(verbose_name="Descripción de la mascota")
    foto_pubm =  models.ImageField(upload_to="PublicMas/", verbose_name="Foto")
    
    #llaves foraneas
    #una mascota solo puede estar publicada una vez
    mascota_pubm = models.OneToOneField(Mascota, verbose_name="Mascota", on_delete=models.CASCADE)
    #Nombres con los que aparece en el panel de administracion
    class Meta:
        verbose_name = "Mascotas Publicadas"
        verbose_name_plural = "Mascotas Publicadas"

    def __str__(self):
        return f"{self.fecha_pubm} - {self.mascota_pubm}"

