from django.contrib import admin
from django.utils.html import format_html

from .models import Raza, Lugar, Medicamento, Mascota, AdministracionMedicamento
# Register your models here.

class AdministracionMedicamentoInline(admin.TabularInline):
    model = AdministracionMedicamento  # La tabla de relación ManyToMany entre Historial y Medicamento
    extra = 0  # Número de formularios en blanco que se mostrarán para agregar nuevos medicamentos

class MascotaAdmin(admin.ModelAdmin):
    inlines = (AdministracionMedicamentoInline,)
    list_display = ("fecha_mas","nombre_mas", "lugar_mas","edad_mas",
		"sexo_mas","esteril_mas", "foto",)
    
    def foto(self, object):
        return format_html('<img src="{}" width="90" height="70" />', object.foto_mas.url)

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ("nombre_med", "precio_med",)

admin.site.register(Raza)
admin.site.register(Lugar)
admin.site.register(Medicamento, MedicamentoAdmin)
admin.site.register(Mascota, MascotaAdmin)
