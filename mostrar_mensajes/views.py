from django.shortcuts import render
from .models import Mensajes
# Create your views here.
def mostrar_mensajes(request):
    mensaje=Mensajes.objects.all()
    return render(request,"mensajes.html",{'mensajes':mensaje})