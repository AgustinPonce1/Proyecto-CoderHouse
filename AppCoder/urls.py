# ALUMNO AGUSTIN LUCAS PONCE DE LEON
# PROYECTO PYTHON - CURSO CODER HOUSE

from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('lista-de-productos/', listar_productos, name="ListaProductos"),
    path('', inicio, name="Inicio"),
    path('productos/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('marcas/', marcas, name="Marcas"),
    path('about-us/', SobreMi, name="SobreMi"),
    path('contacto/', contacto, name="Contacto"),
    #-- FORMULARIOS -- #
    #PRODUCTOS
    path('productos-formulario/', productoFormulario, name="productoFormulario"),
    path('busqueda-producto/', busquedaProducto, name="BusquedaProducto"),
    path('buscar-producto/', buscarProducto, name="BuscarProducto"),
    #CLIENTES
    path('clientes-formulario/', clienteFormulario, name="clienteFormulario"),
    path('busqueda-cliente/', busquedaCliente, name="BusquedaCliente"),
    path('buscar-cliente/', buscarCliente, name="BuscarCliente"),
    #PEDIDOS
    path('pedidos-formulario/', pedidoFormulario, name="pedidoFormulario"),
    path('busqueda-pedido/', busquedaPedido, name="BusquedaPedido"),
    path('buscar-pedido/', buscarPedido, name="BuscarPedido"),
    #PROVEEDORES
    path('proveedores-formulario/', proveedorFormulario, name="proveedorFormulario"),
    path('busqueda-proveedor/', busquedaProveedor, name="BusquedaProveedor"),
    path('buscar-proveedor/', buscarProveedor, name="BuscarProveedor"),
    #LOGIN
    path('login/', loginView, name="Login"),
    #REGISTRO
    path('register/', register, name="Registro"),
    #LOGOUT
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    #AVATAR
    path('agregar-avatar/', agregar_avatar, name="AgregarAvatar"),
    #PERFILES
    path('accounts/usuarios/', user_view, name='Usuarios'),
    path('editar-perfil/', edit_profile, name='editar_perfil'),
    path('profile/change_password/', change_password, name='change_password'),
    #CRUD PRODUCTOS
    path('productos/editar/<int:pk>/', editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', eliminar_producto, name='eliminar_producto'),
    #MESSAGES
    path('messages/', vista_de_mensajes, name='vista_de_mensajes'),
]