from django.db import models
from django.utils import timezone

# Create your models here.

sexos = (
    ("M", "Macho"), 
    ("H", "Hembra"), 
)

especie = (
    ("P", "Perro"), 
    ("G", "Gato"),
)

esteril = (
    ('S', 'Sí'),
    ('N', 'No')
)

#tabla raza
class Raza(models.Model):
    id_raza = models.AutoField(primary_key=True)
    nombre_raza = models.CharField(max_length=50,verbose_name="Raza")
    #Nombres con los que aparece en el panel de administracion
    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas"

    def __str__(self):
            return f"{self.nombre_raza}"

#tabla lugar
class Lugar(models.Model):
    id_lugar = models.AutoField(primary_key=True)
    nombre_lugar = models.CharField(max_length=50,verbose_name="Lugar")
    zona_lugar = models.IntegerField(verbose_name="Zona")
    descripcion = models.CharField(max_length=100,verbose_name="Descripción")
    #Nombres con los que aparece en el panel de administracion
    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"
    
    def __str__(self):
        return f"{self.nombre_lugar}"
    
#tabla medicamento
class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre_med = models.CharField(max_length=50,verbose_name="Nombre Medicamento")
    precio_med = models.DecimalField(max_digits=5, decimal_places=2, default=0,verbose_name="Precio")
    descripcion_med = models.CharField(max_length=150,verbose_name="Descripción")

    def __str__(self):
        return f"{self.nombre_med} - Q.{self.precio_med}"

#tabla mascota
class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    fecha_mas = models.DateField(default=timezone.now,verbose_name="Fecha de rescate")
    nombre_mas = models.CharField(max_length=50,verbose_name="Nombre")
    especie_mas = models.CharField(choices = especie, default = 'P', max_length = 20,verbose_name="Especie")
    sexo_mas = models.CharField(choices = sexos, default = 'M', max_length = 20,verbose_name="Sexo")
    edad_mas = models.IntegerField(verbose_name="Edad aproximada")
    color_mas = models.CharField(max_length= 30,verbose_name="Color")
    observacion_mas = models.CharField(max_length = 100,verbose_name="Observaciones", blank=True)
    esteril_mas = models.CharField(choices = esteril, default = 'N', max_length = 20,verbose_name="¿Esterilizado?")
    foto_mas =  models.ImageField(upload_to="mascota", verbose_name="Foto")
    active = models.BooleanField(default=True,verbose_name="Activo")
    created = models.DateField(auto_now_add=True)

    #llaves foraneas
    #una mascota puede pertenecer a una raza y a un lugar de rescate
    raza_mas = models.ForeignKey(Raza, verbose_name="Raza", on_delete=models.CASCADE)
    lugar_mas = models.ForeignKey(Lugar, verbose_name="Lugar de rescate", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_mas}"


#Tabla para historial
class AdministracionMedicamento(models.Model):
    id_administracion = models.AutoField(primary_key=True)
    fecha_administracion = models.DateField(default=timezone.now, verbose_name="Fecha de administración")
    dosis_administrada = models.CharField(max_length=50, verbose_name="Dosis administrada", blank=True)
    mascota = models.ForeignKey(Mascota, related_name='Mascota', on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, related_name='Medicamento', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.mascota.nombre_mas} - {self.medicamento.nombre_med} - {self.fecha_administracion}"