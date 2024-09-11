from django.shortcuts import render

from django.http.response import JsonResponse

# Create your views here.


def indexMascota(request):
    return render(request, "indexMascota.html")


def get_chart(request):
    chart = {
        
    }

    return JsonResponse(chart)
