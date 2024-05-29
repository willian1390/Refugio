from django.contrib import admin
from django.utils.html import format_html

from .models import Categoria, Blog, Publicar_Mas

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("titulo_blog","imagen",)


    def imagen(self, object):
        return format_html('<img src="{}" width="90" height="70" />', object.foto_blog.url)

class Publicar_Mas_Admin(admin.ModelAdmin):
    list_display = ("mascota_pubm","imagen",)


    def imagen(self, object):
        return format_html('<img src="{}" width="90" height="70" />', object.foto_pubm.url)

admin.site.register(Categoria)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Publicar_Mas, Publicar_Mas_Admin)


    