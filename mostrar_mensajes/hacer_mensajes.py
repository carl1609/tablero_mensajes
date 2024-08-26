from models import mensajes

def generar_mesajes(contenido,remitente,destinatario):
    men=mensajes(texto_mensaje=contenido,remitente=remitente,destinatario=destinatario)
    men.save()

generar_mesajes("barrer la casa","mama","hijo")
generar_mesajes("corregir el puento dos de la tarea","profesor","jaimito")


#error
#Traceback (most recent call last):
 # File "/home/cmario/Escritorio/django/proyectos/tablero_mensajes/tablero_mensajes/mostrar_mensajes/hacer_mensajes.py", line 1, in <module>
   # from models import mensajes
  #File "/home/cmario/Escritorio/django/proyectos/tablero_mensajes/tablero_mensajes/mostrar_mensajes/models.py", line 4, in <module>
   # class mensajes(models.Model):
  #File "/home/cmario/Escritorio/django/entornos/tablero_mensajes/tablero_mensajes/lib/python3.10/site-packages/django/db/models/base.py", line 129, in __new__
   # app_config = apps.get_containing_app_config(module)
  #File "/home/cmario/Escritorio/django/entornos/tablero_mensajes/tablero_mensajes/lib/python3.10/site-packages/django/apps/registry.py", line 260, in get_containing_app_config
   # self.check_apps_ready()
  #File "/home/cmario/Escritorio/django/entornos/tablero_mensajes/tablero_mensajes/lib/python3.10/site-packages/django/apps/registry.py", line 137, in check_apps_ready
   # settings.INSTALLED_APPS
  #File "/home/cmario/Escritorio/django/entornos/tablero_mensajes/tablero_mensajes/lib/python3.10/site-packages/django/conf/__init__.py", line 102, in __getattr__
   # self._setup(name)
  #File "/home/cmario/Escritorio/django/entornos/tablero_mensajes/tablero_mensajes/lib/python3.10/site-packages/django/conf/__init__.py", line 82, in _setup
   # raise ImproperlyConfigured(
#django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.