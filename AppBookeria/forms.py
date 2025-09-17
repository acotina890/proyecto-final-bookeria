from django import forms


# formulario para agregar libros (base de datos)
class AgregarLibro(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    editorial = forms.CharField()
    stock = forms.IntegerField()
    precio = forms.CharField()
    oferta = forms.CharField()


# formulario para buscar libros por título en específico (base de datos)
class BuscarTitulo(forms.Form):
    titulo = forms.CharField()



# formulario para buscar libros por autor en específico (base de datos)
class BuscarAutor(forms.Form):
    autor = forms.CharField()



# formulario para buscar libros por editorial en específico (base de datos)
class BuscarEditorial(forms.Form):
    editorial = forms.CharField()


# formulario para buscar libros a oferta (base de datos)
class BuscarOfertas(forms.Form):
    titulo = forms.CharField()









# formulario para registrar compras realizadas por los usuarios (base de datos)
class RegistrarCompra(forms.Form):
    usuario = forms.CharField()
    libro = forms.CharField()
    oferta = forms.CharField()
    precio = forms.CharField()
    pago = forms.CharField()
    fecha = forms.CharField()


# formulario para buscar compras ingresando el nombre de usuario
class BuscarCompra(forms.Form):
    usuario = forms.CharField()











# formulario para que el usuario se registre
class RegistroUsuario(forms.Form):
    user = forms.CharField() # nombre de usuario
    nombre = forms.CharField() # nombre de la persona
    apellido = forms.CharField()
    correo = forms.CharField()
    clave = forms.CharField()


# formulario para buscar un usuario en la base de datos
class BuscarUsuario(forms.Form):
    user = forms.CharField()