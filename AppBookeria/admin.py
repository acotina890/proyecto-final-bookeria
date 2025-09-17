from django.contrib import admin
from AppBookeria.models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Compra)
admin.site.register(Libro)




# INGRESAR CON ESTOS DATOS AL ADMIN DJANGO (super usuario)
# USUARIO: Laura
# CONTRASEÑA: abcd1234