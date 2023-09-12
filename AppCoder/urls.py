# ALUMNO AGUSTIN LUCAS PONCE DE LEON
# PROYECTO PYTHON - CURSO CODER HOUSE

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('lista-de-productos/', listar_productos, name="ListaProductos"),
    path('', inicio, name="Inicio"),
    path('productos/', productos, name="Productos"),
    path('marcas/', marcas, name="Marcas"),
    path('sobreNosotros/', sobreNosotros, name="SobreNosotros"),
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
]
