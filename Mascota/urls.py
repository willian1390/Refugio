from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexMascota, name='indexMascota'),
    path('get_chart/', views.get_chart, name='get_chart')
]