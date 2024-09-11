from django.contrib import admin
from django.utils.html import format_html

from .models import Categoria, Blog, Publicar_Mas

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("titulo_blog","imagen", "creado_blog",)


    def imagen(self, object):
        return format_html('<img src="{}" width="90" height="70" />', object.foto_blog.url)

class Publicar_Mas_Admin(admin.ModelAdmin):
    list_display = ("mascota_pubm","imagen", 'fecha_pubm',)
    autocomplete_fields = ['mascota_pubm']


    def imagen(self, object):
        return format_html('<img src="{}" width="90" height="70" />', object.foto_pubm.url)

admin.site.register(Categoria)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Publicar_Mas, Publicar_Mas_Admin)


admin.site.site_header = "Asociación SIRIUS"
admin.site.index_title = "Panel de administración"
admin.site.site_title = "SIRIUS"