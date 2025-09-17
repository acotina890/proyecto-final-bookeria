# importación de librerías
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# importación de modelos
from AppBookeria.models import Usuario, Compra, Libro
from AppBookeria.forms import *



# Create your views here.

# funciones para el NAVBAR
def pag_inicio(request): # mostrar página inicio
    return render(request, 'AppBookeria/inicio.html')

def pag_libros(request): # mostrar página libros
    return render(request, 'AppBookeria/libros/libros.html')

def pag_ofertas(request): # mostrar página ofertas
    return render(request, 'AppBookeria/ofertas/ofertas.html')

def pag_compras(request): # mostrar página compras
    return render(request, 'AppBookeria/compras/compras.html')





# SISTEMA LOGIN: REGISTRAR / INICIAR SESIÓN---------------------------------------------------------------c


# función para iniciar sesión, EN DESARROLLO
def login_usuario(request): 
    return render(request, 'AppBookeria/usuarios/login.html') # cargar archivo html



# registrar datos de usuario en la base de datos
def registro_usuario(request):
    if request.method == "POST":
        form = RegistroUsuario(request.POST) # uso de formulario

        if form.is_valid():
            info = form.cleaned_data

            usuario = Usuario( # uso de modelo
                user = info["user"],
                nombre = info["nombre"],
                apellido = info["apellido"],
                correo = info["correo"],
                clave = info["clave"]
            )

            usuario.save() # cargar los datos recibidos en la base de datos

            return render(request, "AppBookeria/usuarios/login.html") # cargar archivo html formulario
        
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
    
    else:
        form = RegistroUsuario()
    

    return render(request, "AppBookeria/usuarios/registroUsuarioForm.html") # cargar archivo html formulario



# función para buscar por nombre de usuario en la base de datos
def buscar_usuario(request):
    if request.method == "POST":
        form = BuscarUsuario(request.POST) # uso de formulario

        if form.is_valid():
            info = form.cleaned_data

            usuarios = Usuario.objects.filter(user__icontains = info["user"]) # para buscar datos en la base de datos

            return render(request, "AppBookeria/usuarios/resultBusqUsuario.html", {"usuarios":usuarios}) # pasaje de datos al archivo html
        
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
        
    else:
        form = BuscarUsuario()
    

    return render(request, "AppBookeria/usuarios/busqUsuarioForm.html") # cargar archivo html formulario



# función para mostrar todos los datos de usuarios registrados en la base de datos
def lista_usuarios(request):
    todos_los_usuarios = Usuario.objects.all() # almacenamiento de datos
    return render(request, "AppBookeria/usuarios/listadoUsuarios.html", {"usuarios":todos_los_usuarios}) # pasaje de datos al archivo html














# SISTEMA COMPRAS: REGISTRAR / BUSCAR-----------------------------------------------------------------------

# función registrar compras en la base de datos
def registrar_compra(request):

    if request.method == "POST":

        form = RegistrarCompra(request.POST) # uso de formulario

        if form.is_valid():

            info = form.cleaned_data

            compra = Compra( # uso de modelo
                usuario = info["usuario"],
                libro = info["libro"],
                oferta = info["oferta"],
                precio = info["precio"],
                pago = info["pago"],
                fecha = info["fecha"]
            )

            compra.save() # guardar datos en la base de datos

            return render(request, "AppBookeria/compras/compras.html")
        
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
    
    else:
        form = RegistrarCompra()
    
    return render(request, "AppBookeria/compras/registrarCompraForm.html")





# función para buscar compras de un usuario en específico
def buscar_compra(request):
    if request.method == "POST":

        form = BuscarCompra(request.POST) # uso de formulario

        if form.is_valid():
            info = form.cleaned_data

            compras = Compra.objects.filter(usuario__icontains = info["usuario"]) # uso de modelo

            return render(request, "AppBookeria/compras/resultBusqComp.html", {"compras":compras}) # pasaje de datos al archivo html
        
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
    
    else:
        form = BuscarCompra()

    return render(request, "AppBookeria/compras/busqCompraForm.html") # cargar archivo html formulario





# función para mostrar todas las compras hechas
def lista_compras(request):
    todas_las_compras = Compra.objects.all() # almacenamiento de datos de la bd
    return render(request, "AppBookeria/compras/listadoCompras.html", {"compras":todas_las_compras}) # pasaje de datos al archivo html







# función para página inicio: REGISTRAR LIBRO 1 (Harry Potter)
def comprar_def1(request):
    if request.method == "POST":
        form = RegistrarCompra(request.POST) # uso de formulario

        if form.is_valid():

            info = form.cleaned_data

            compra = Compra( # uso de modelo
                usuario = info["usuario"],
                libro = info["libro"],
                oferta = info["oferta"],
                precio = info["precio"],
                pago = info["pago"],
                fecha = info["fecha"]
            )

            compra.save() # guardar datos en la base de datos

            return render(request, "AppBookeria/compras/compras.html") # cargar página compras
        
        else:

            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
    
    else:
        form = RegistrarCompra()
    
    return render(request, "AppBookeria/compras/defaultForms/regCompForm1.html") # cargar archivo html formulario






# función para página inicio: REGISTRAR LIBRO 2 (Crisis)
def comprar_def2(request):

    if request.method == "POST":

        form = RegistrarCompra(request.POST) # uso de formulario

        if form.is_valid():

            info = form.cleaned_data

            compra = Compra( # uso de modelo
                usuario = info["usuario"],
                libro = info["libro"],
                oferta = info["oferta"],
                precio = info["precio"],
                pago = info["pago"],
                fecha = info["fecha"]
            )

            compra.save() # guardar datos en la base de datos

            return render(request, "AppBookeria/compras/compras.html") # cargar página compras
        
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
    
    else:
        form = RegistrarCompra()
    
    return render(request, "AppBookeria/compras/defaultForms/regCompForm2.html") # cargar archivo html formulario






# función para página inicio: REGISTRAR LIBRO 3 (Bocabesada)
def comprar_def3(request):

    if request.method == "POST":

        form = RegistrarCompra(request.POST) # uso de formulario

        if form.is_valid():

            info = form.cleaned_data

            compra = Compra( # uso de modelo
                usuario = info["usuario"],
                libro = info["libro"],
                oferta = info["oferta"],
                precio = info["precio"],
                pago = info["pago"],
                fecha = info["fecha"]
            )

            compra.save() # guardar datos en la base de datos

            return render(request, "AppBookeria/compras/compras.html") # cargar página compras
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
    
    else:
        form = RegistrarCompra()
    
    return render(request, "AppBookeria/compras/defaultForms/regCompForm3.html") # cargar archivo html formulario






# función para página inicio: REGISTRAR LIBRO 4 (Regla Mola)
def comprar_def4(request):

    if request.method == "POST":

        form = RegistrarCompra(request.POST) # uso de formulario


        if form.is_valid():

            info = form.cleaned_data

            compra = Compra( # uso de modelo
                usuario = info["usuario"],
                libro = info["libro"],
                oferta = info["oferta"],
                precio = info["precio"],
                pago = info["pago"],
                fecha = info["fecha"]
            )

            compra.save() # guardar datos en la base de datos

            return render(request, "AppBookeria/compras/compras.html") # cargar página compras
        
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
    
    else:
        form = RegistrarCompra()
    
    return render(request, "AppBookeria/compras/defaultForms/regCompForm4.html") # cargar archivo html formulario





# función para página inicio: REGISTRAR LIBRO 5 (The walking dead)
def comprar_def5(request):

    if request.method == "POST":

        form = RegistrarCompra(request.POST) # uso de formulario

        if form.is_valid():

            info = form.cleaned_data

            compra = Compra( # uso de modelo
                usuario = info["usuario"],
                libro = info["libro"],
                oferta = info["oferta"],
                precio = info["precio"],
                pago = info["pago"],
                fecha = info["fecha"]
            )

            compra.save() # guardar datos en la base de datos

            return render(request, "AppBookeria/compras/compras.html") # cargar página compras
        
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
    
    else:
        form = RegistrarCompra()
    
    return render(request, "AppBookeria/compras/defaultForms/regCompForm5.html") # cargar archivo html formulario






# función para página inicio: REGISTRAR LIBRO 6 (El principito)
def comprar_def6(request):

    if request.method == "POST":

        form = RegistrarCompra(request.POST) # uso de formulario

        if form.is_valid():

            info = form.cleaned_data

            compra = Compra( # uso de modelo
                usuario = info["usuario"],
                libro = info["libro"],
                oferta = info["oferta"],
                precio = info["precio"],
                pago = info["pago"],
                fecha = info["fecha"]
            )

            compra.save() # guardar datos en la base de datos

            return render(request, "AppBookeria/compras/compras.html") # cargar página compras
        
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
    
    else:
        form = RegistrarCompra()
    
    return render(request, "AppBookeria/compras/defaultForms/regCompForm6.html") # cargar archivo html formulario






# función para página inicio: REGISTRAR LIBRO 7 (Beyond)
def comprar_def7(request):

    if request.method == "POST":

        form = RegistrarCompra(request.POST) # uso de formulario

        if form.is_valid():

            info = form.cleaned_data

            compra = Compra( # uso de modelo
                usuario = info["usuario"],
                libro = info["libro"],
                oferta = info["oferta"],
                precio = info["precio"],
                pago = info["pago"],
                fecha = info["fecha"]
            )

            compra.save() # guardar datos en la base de datos

            return render(request, "AppBookeria/compras/compras.html") # cargar página compras
        
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
    
    else:
        form = RegistrarCompra()
    
    return render(request, "AppBookeria/compras/defaultForms/regCompForm7.html") # cargar página archivo html formulario







# función para página inicio: REGISTRAR LIBRO 8 (Diario de Ana)
def comprar_def8(request):

    if request.method == "POST":

        form = RegistrarCompra(request.POST) # uso de formulario


        if form.is_valid():

            info = form.cleaned_data

            compra = Compra( # uso de modelo
                usuario = info["usuario"],
                libro = info["libro"],
                oferta = info["oferta"],
                precio = info["precio"],
                pago = info["pago"],
                fecha = info["fecha"]
            )

            compra.save() # guardar datos en la base de datos

            return render(request, "AppBookeria/compras/compras.html") # cargar página compras
        
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
    
    else:
        form = RegistrarCompra()
    
    return render(request, "AppBookeria/compras/defaultForms/regCompForm8.html") # cargar archivo html formulario
















# SISTEMA LIBROS: REGISTRAR / BUSCAR-----------------------------------------------------------------------

# función registrar libros a la base de datos
def agregar_libros(request):

    if request.method == "POST":

        form = AgregarLibro(request.POST) # uso de formulario

        if form.is_valid():

            info = form.cleaned_data

            libro = Libro( # uso de modelo
                    titulo = info["titulo"],
                    autor = info["autor"],
                    editorial = info["editorial"],
                    stock = info["stock"],
                    precio = info["precio"],
                    oferta = info["oferta"]
                )
            
            libro.save() # guardar datos en la base de datos

            return render(request, "AppBookeria/libros/libros.html") # cargar página libros
        
        else:
            print("Formulario inválido") # guía para el programador en caso que la carga de datos no ha funcionado
        
    else:
        form = AgregarLibro()
    

    return render(request, "AppBookeria/libros/agregarLibrosForm.html") # cargar archivo html formulario
    





# función para buscar libros por título
def buscar_titulo(request):

    if request.method == "POST":

        form = BuscarTitulo(request.POST) # uso de formulario

        if form.is_valid():
            info = form.cleaned_data

            libros = Libro.objects.filter(titulo__icontains = info["titulo"]) # guardar datos recibidos

            return render(request, "AppBookeria/libros/resultBusqTitulos.html", {"libros":libros}) # pasaje de datos al archivo html
    else:
        form = BuscarTitulo()
    

    return render(request, "AppBookeria/libros/buscarTitulosForm.html") # cargar archivo html formulario





# función para buscar libros por autor
def buscar_autor(request):

    if request.method == "POST":

        form = BuscarAutor(request.POST) # uso de formulario


        if form.is_valid():
            info = form.cleaned_data

            libros = Libro.objects.filter(autor__icontains = info["autor"]) # guardar datos recibidos

            return render(request, "AppBookeria/libros/resultBusqAutor.html", {"libros":libros}) # pasaje de datos al archivo html
        
    else:
        form = BuscarAutor()
    

    return render(request, "AppBookeria/libros/buscarAutorForm.html") # cargar archivo html formulario





# función para buscar libros por editorial
def buscar_editorial(request):

    if request.method == "POST":

        form = BuscarEditorial(request.POST) # uso de formulario


        if form.is_valid():
            info = form.cleaned_data

            libros = Libro.objects.filter(editorial__icontains = info["editorial"]) # guardar datos recibidos

            return render(request, "AppBookeria/libros/resultBusqEditorial.html", {"libros":libros}) # pasaje de datos al archivo html
        
    else:
        form = BuscarEditorial()
    

    return render(request, "AppBookeria/libros/buscarEditorialForm.html") # cargar archivo html formulario




# función para mostrar todos los libros registrados
def lista_libros(request):
    todos_los_libros = Libro.objects.all() # guardar datos de la base de datos

    return render(request, "AppBookeria/libros/listadoLibros.html", {"libros":todos_los_libros}) # pasaje de datos al archivo html











# SISTEMA LIBROS: BUSCAR / LISTAR-----------------------------------------------------------------------

# función para buscar ofertas disponibles
def buscar_ofertas(request):

    if request.method == "POST":

        form = BuscarOfertas(request.POST) # uso de formulario


        if form.is_valid():
            info = form.cleaned_data

            libros = Libro.objects.filter(titulo__icontains = info["titulo"]) # guardar datos recibidos

            return render(request, "AppBookeria/ofertas/resultBusqOfertas.html", {"libros":libros}) # pasaje de datos al archivo html
        
    else:
        form = BuscarOfertas()
    

    return render(request, "AppBookeria/ofertas/buscarOfertasForm.html") # cargar archivo html formulario




# función mostrar todas las ofertas disponibles
def lista_ofertas(request):
    todas_las_ofertas = Libro.objects.all() # guardar datos de la base de datos

    return render(request, "AppBookeria/ofertas/listadoOfertas.html", {"libros":todas_las_ofertas}) # pasaje de datos al archivo html