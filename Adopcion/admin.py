from django.contrib import admin

#importar modelos
from .models import Persona, Adopcion

# Register your models here.

class AdopcionInline(admin.TabularInline):
    model = Adopcion
    extra = 0


class PersonaAdmin(admin.ModelAdmin):
    inlines = (AdopcionInline,)
    list_display = ("dpi_persona", "nombre_p", "apellido_p", "adoptados",)

    def adoptados(self, obj):
        adopciones = obj.adopciones.all()
        return ", ".join([adopcion.mascota_adop.nombre_mas for adopcion in adopciones])
    
    adoptados.short_description = 'Adoptados'

class AdopcionAdmin(admin.ModelAdmin):
    list_display = ( "fecha_adop", "mascota_adop", "persona_adop", )



admin.site.register(Persona, PersonaAdmin)
admin.site.register(Adopcion, AdopcionAdmin)