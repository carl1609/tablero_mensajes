from .models import mensajes

def generar_mesajes(contenido,remitente,destinatario):
    men=mensajes(texto_mensaje=contenido,remitente=remitente,destinatario=destinatario)
    men.save()

generar_mesajes("barrer la casa","mama","hijo")
generar_mesajes("corregir el puento dos de la tarea","profesor","jaimito")
