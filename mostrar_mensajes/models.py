from django.db import models

# Create your models here.
class Mensajes(models.Model):
    texto_mensaje=models.TextField()
    remitente=models.TextField()
    destinatario=models.TextField()
    fecha_hora= models.DateTimeField(auto_now=True) 