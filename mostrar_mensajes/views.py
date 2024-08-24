from django.shortcuts import render
from .models import mensajes
# Create your views here.
def mostrar_mensajes(request):
    mensaje=mensajes.objects.all()
    return render(request,"mensajes.html",{'mensajes':mensaje})