from django.shortcuts import render

#importar modelos
from .models import Publicar_Mas, Blog
# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    blog = Blog.objects.all()
    return render(request, "blog.html", {"blog": blog})

def mascota_p(request):
    mascota_p = Publicar_Mas.objects.filter(active = True)
    return render(request, 'mascota_p.html', {'mascota_p': mascota_p})

def ayuda(request):
    return render(request, 'ayuda.html')

def contacto(request):
    return render(request, 'contacto.html')