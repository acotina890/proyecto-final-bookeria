from django.db import models


# Create your models here.
class Usuario(models.Model): # persona a comprar el libro
    user = models.CharField(max_length=100) # nombre usuario
    nombre = models.CharField(max_length=100) # nombre persona
    apellido = models.CharField(max_length=100) # apellido
    correo = models.CharField(max_length=100) # correo
    clave = models.CharField(max_length=100) # contraseña


# registrar la compra por el usuario y le figure en su historial
class Compra(models.Model):
    usuario = models.CharField(max_length=100) # quién está comprando
    libro = models.CharField(max_length=200) # qué libro compra
    oferta = models.CharField(max_length=50) # descuento en el precio
    precio = models.CharField(max_length=100) # cantidad final a pagar
    pago = models.CharField(max_length=50) # con qué paga / método de pago
    fecha = models.CharField(max_length=50) # cuándo realiza / realizó la compra



# producto de la web para ser comprado
class Libro(models.Model):
    titulo = models.CharField(max_length=200) # nombre del libro
    autor = models.CharField(max_length=100) # quién escribió el libro
    editorial = models.CharField(max_length=100) # quién distribuyó el libro
    stock = models.IntegerField() # cantidad disponible restante
    precio = models.CharField(max_length=100) # cantidad a pagar
    oferta = models.CharField(max_length=50) # descuento en el precio