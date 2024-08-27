# hacer_mensajes.py
import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tablero_mensajes.settings')
django.setup()

from mostrar_mensajes.models import Mensajes

def generar_mensajes(contenido, remitente, destinatario):
    men = Mensajes(texto_mensaje=contenido, remitente=remitente, destinatario=destinatario)
    men.save()

generar_mensajes("barrer la casa", "mama", "hijo")
generar_mensajes("corregir el punto dos de la tarea", "profesor", "jaimito")

