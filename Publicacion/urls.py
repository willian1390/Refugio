from django.urls import path

#Importar vistas
from Publicacion import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('mascota_p/', views.mascota_p, name='mascota_p'),
    path('ayuda/', views.ayuda, name='ayuda'),
    path('contacto/', views.contacto, name='contacto'),
]