from django.db import models
#from django.utils import timezone
from PIL import Image

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
    contenido_blog = models.TextField(verbose_name="Contenido")
    creado_blog = models.DateField(auto_now_add=True, verbose_name="Fecha de publicación")
    #llaves foraneas
    #un blog puede tener una o muchas categorias
    categoria_blog = models.ForeignKey(Categoria, verbose_name="Categoría", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo_blog}"

#tabla Publicar Mascota
class Publicar_Mas(models.Model):
    id_pubm =models.AutoField(primary_key=True)
    fecha_pubm = models.DateField(auto_now_add=True, verbose_name="Fecha de publicación")
    descripcion_pubm = models.TextField(verbose_name="Descripción de la mascota")
    foto_pubm =  models.ImageField(upload_to="PublicMas/", verbose_name="Foto")
    active = models.BooleanField(default=True,verbose_name="Activo")
    
    #llaves foraneas
    #una mascota solo puede estar publicada una vez
    mascota_pubm = models.OneToOneField(Mascota, verbose_name="Mascota", on_delete=models.CASCADE)
    #Nombres con los que aparece en el panel de administracion
    class Meta:
        verbose_name = "Mascotas Publicadas"
        verbose_name_plural = "Mascotas Publicadas"

    def __str__(self):
        return f"{self.fecha_pubm} - {self.mascota_pubm}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Ruta de la imagen recién guardada
        img_path = self.foto_pubm.path
        # Abrir la imagen usando Pillow
        img = Image.open(img_path)
        # Definir el tamaño al que deseas recortar la imagen
        target_size = (1000, 1000)
        
        # Obtener el tamaño original de la imagen
        img_width, img_height = img.size
        
        # Calcular las coordenadas del recorte para centrar la imagen
        left = (img_width - target_size[0]) / 2
        top = (img_height - target_size[1]) / 2
        right = (img_width + target_size[0]) / 2
        bottom = (img_height + target_size[1]) / 2
        
        # Asegurarse de que las coordenadas no excedan los límites de la imagen
        if left < 0: left = 0
        if top < 0: top = 0
        if right > img_width: right = img_width
        if bottom > img_height: bottom = img_height
        
        # Recortar la imagen
        img = img.crop((left, top, right, bottom))
        # Guardar la imagen recortada
        img.save(img_path)