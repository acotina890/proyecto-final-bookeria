# importación de librerías
from django.urls import path
from AppBookeria import views


# lista de urls
urlpatterns = [

    # urls principales: NAVBAR
    path('', views.pag_inicio, name="Inicio"), # página inicio
    path('libros/', views.pag_libros, name="Libros"), # página libros
    path('ofertas/', views.pag_ofertas, name="Ofertas"), # página ofertas
    path('compras/', views.pag_compras, name="Compras"), # página compras


    # urls sistema COMPRAS
    path('registrar-compra/', views.registrar_compra, name="RegistrarCompra"), # página registrar compra
    path('buscar-compra/', views.buscar_compra, name="BuscarCompra"), # página búsqueda compra
    path('lista-compras/', views.lista_compras, name='ListaCompras'), # página listado compras


    # urls COMPRAS de la PÁGINA INICIO
    path('comprar-1/', views.comprar_def1, name="Comprar1"), # página comprar Libro 1 (Harry Potter)
    path('comprar-2/', views.comprar_def2, name="Comprar2"), # página comprar Libro 2 (Crisis)
    path('comprar-3/', views.comprar_def3, name="Comprar3"), # página comprar Libro 3 (Bocabesada)
    path('comprar-4/', views.comprar_def4, name="Comprar4"), # página comprar Libro 4 (Regla Mola)
    path('comprar-5/', views.comprar_def5, name="Comprar5"), # página comprar Libro 5 (The walking dead)
    path('comprar-6/', views.comprar_def6, name="Comprar6"), # página comprar Libro 6 (El principito)
    path('comprar-7/', views.comprar_def7, name="Comprar7"), # página comprar Libro 7 (Beyond)
    path('comprar-8/', views.comprar_def8, name="Comprar8"), # página comprar Libro 8 (Diario Ana Frank)


    # urls sistema LOGIN (usuarios)
    path('login/', views.login_usuario, name="Login"), # página en desarrollo, falta mejorar
    path('registro-usuario/', views.registro_usuario, name='RegistroUsuario'), # página registrar 
    path('busqueda-usuarios/', views.buscar_usuario, name="BuscarUsuario"), # página búsqueda usuarios
    path('lista-usuarios/', views.lista_usuarios, name="ListaUsuarios"), # página listado usuarios


    # urls sistema LIBROS
    path('agregar-libros/', views.agregar_libros, name="AgregarLibros"), # página agregar libros
    path('busqueda-libros-titulos/', views.buscar_titulo, name="BuscarTitulo"), # página búsqueda por títulos
    path('busqueda-libros-autor/', views.buscar_autor, name="BuscarAutor"), # página búsqueda por autor
    path('busqueda-libros-editorial/', views.buscar_editorial, name="BuscarEditorial"), # página búsqueda por editorial
    path('lista-libros/', views.lista_libros, name="ListaLibros"), # página listado libros


    # urls sistema OFERTAS
    path('busqueda-ofertas/', views.buscar_ofertas, name="BuscarOfertas"), # página búsqueda ofertas
    path('lista-ofertas/', views.lista_ofertas, name="ListaOfertas") # página listado ofertas
]