from django.db import models


#Importacion de modelos
from Mascota.models import Mascota
# Create your models here.

class Persona(models.Model):
    dpi_persona=models.IntegerField(primary_key=True, verbose_name="DPI")
    nombre_p = models.CharField(max_length=50,verbose_name="Nombres")
    apellido_p = models.CharField(max_length=50,verbose_name="Apellidos")
    edad_p = models.IntegerField(verbose_name="Edad")
    direccion_p = models.CharField(max_length=50,verbose_name="Dirección")
    telefono_p = models.CharField(max_length=50,verbose_name="Teléfono")
    redes_p = models.CharField(max_length=50,verbose_name="Redes")

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Crear Adopción"

    def __str__ (self):
        return f"{self.nombre_p} {self.apellido_p}"

class Adopcion(models.Model):
    id_adopcion = models.AutoField(primary_key=True)
    fecha_adop = models.DateField(auto_now_add=True)
    preguntas_adop = models.TextField(default="preguntas para adoptar",verbose_name="Formulario")
    
    #llaves foraneas
    #una persona puede realizar varias adopciones
    persona_adop = models.ForeignKey(Persona, verbose_name="Adoptante", on_delete=models.CASCADE, related_name='adopciones')
    #una mascota solo puede ser adoptada una vez
    mascota_adop = models.OneToOneField(Mascota, verbose_name="Mascota", on_delete=models.CASCADE)
    #Nombres con los que aparece en el panel de administracion
    class Meta:
        verbose_name = "Adopción"
        verbose_name_plural = "Mascotas adoptadas"

    def __str__(self):
        return f"{self.fecha_adop} - {self.mascota_adop} - {self.persona_adop}"
    


    