from django.shortcuts import render
from .models import Place, People


# Create your views here.

def demo(request):
    obj = Place.objects.all()
    obt = People.objects.all()

    return render(request, "index.html", {'result': obj, 'result1': obt})
