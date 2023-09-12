# ALUMNO AGUSTIN LUCAS PONCE DE LEON
# PROYECTO PYTHON - CURSO CODER HOUSE

from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpRequest
from .forms import *
from django.db.models import Q #Añadi esta clase para los formularios y realizar las busquedas de filtro más complejas y flexibles

# Create your views here.
def producto(req, nombre, marca):
    producto = Producto(nombre=nombre, marca=marca)
    producto.save()
    return HttpResponse(f"""
    <p>Producto: {producto.nombre} - Marca: {producto.marca} creado con éxito!</p>
    """)

def listar_productos(req):
    lista = Producto.objects.all()
    return render(req, "lista_productos.html", {"lista_productos": lista})

def inicio(req):
    return render(req, 'inicio.html')

def productos(req):
    return render(req, 'productos.html')

def marcas(req):
    return render(req, 'marcas.html')

def sobreNosotros(req):
    return render(req, 'sobreNosotros.html')

def contacto(req):
    return render(req, 'contacto.html')

#FORMULARIO CLASE PRODUCTO
def productoFormulario(req):
    if req.method == 'POST':
        miFormulario = ProductoFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nombre = data['producto']
            marca = data['marca']
            talle = data['talle']
            precio = data['precio']
            producto_existente = Producto.objects.filter(nombre=nombre, marca=marca,talle=talle, precio=precio).first()
            if producto_existente:
                return HttpResponse(f'Ya existe este producto!')
            else:
                producto = Producto(nombre=nombre, marca=marca, talle=data['talle'], precio=precio)
                producto.save()
                return render(req, 'inicio.html')
    else:
        miFormulario = ProductoFormulario()
    return render(req, 'productoFormulario.html', {"miFormulario": miFormulario})
    
def busquedaProducto(req):
    return render(req, 'busquedaProducto.html')

def buscarProducto(request):
    consulta = request.GET.get('consulta', '')

    if consulta:
        productos = Producto.objects.filter(
            Q(nombre__icontains=consulta) |
            Q(marca__icontains=consulta) |
            Q(descripcion__icontains=consulta) |
            Q(talle__icontains=consulta)
        )
        return render(request, 'resultadosBusqueda.html', {"resultados": productos, "modelo": "Productos"})
    else:
        mensaje_error = "Por favor, ingresa un término de búsqueda para buscar productos."
        return render(request, 'errorBusqueda.html', {"mensaje_error": mensaje_error})

#FORMULARIO CLASE CLIENTE
def clienteFormulario(req):
    if req.method == 'POST':
        miFormulario = ClienteFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nombre = data['nombre']
            apellido = data['apellido']
            cliente_existente = Cliente.objects.filter(nombre=nombre, apellido=apellido).first()
            if cliente_existente:
                return HttpResponse(f'Ya existe este cliente!')
            else:
                client = Cliente(nombre=nombre, apellido=apellido, email=data['email'])
                client.save()
                return render(req, 'inicio.html')
    else:
        miFormulario = ClienteFormulario()
    return render(req, 'clienteFormulario.html', {"miFormulario": miFormulario})
    
def busquedaCliente(req):
    return render(req, 'busquedaCliente.html')
    
def buscarCliente(request):
    consulta = request.GET.get('consulta', '')

    if consulta:
        clientes = Cliente.objects.filter(
            Q(nombre__icontains=consulta) |
            Q(apellido__icontains=consulta) |
            Q(email__icontains=consulta)
        )
        return render(request, 'resultadosBusqueda.html', {"resultados": clientes, "modelo": "Clientes"})
    else:
        mensaje_error = "Por favor, ingresa un término de búsqueda para buscar clientes."
        return render(request, 'errorBusqueda.html', {"mensaje_error": mensaje_error})

#FORMULARIO CLASE PEDIDO
def pedidoFormulario(req):
    if req.method == 'POST':
        miFormulario = PedidoFormulario(req.POST)
        if miFormulario.is_valid():
            miFormulario.save()  # Guardar el pedido en la base de datos
            return render(req, 'inicio.html')  # O redirige a donde desees

    else:
        miFormulario = PedidoFormulario()

    return render(req, 'pedidoFormulario.html', {"miFormulario": miFormulario})
    
def busquedaPedido(req):
    return render(req, 'busquedaPedido.html')

def buscarPedido(request):
    consulta = request.GET.get('consulta', '')

    if consulta:
        pedidos = Pedido.objects.filter(
            Q(cliente__nombre__icontains=consulta) |
            Q(cliente__apellido__icontains=consulta) |
            Q(cliente__email__icontains=consulta) |
            Q(productos__marca__icontains=consulta)
        )
        return render(request, 'resultadosBusqueda.html', {"resultados": pedidos, "modelo": "Pedidos"})
    else:
        mensaje_error = "Por favor, ingresa un término de búsqueda para buscar pedidos."
        return render(request, 'errorBusqueda.html', {"mensaje_error": mensaje_error})

#FORMULARIO CLASE PROVEEDOR
def proveedorFormulario(req):
    if req.method == 'POST':
        miFormulario = ProveedorFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            empresa = data['empresa']
            direccion = data['direccion']
            telefono = data['telefono']
            proveedor_existente = Proveedor.objects.filter(empresa=empresa).first()
            if proveedor_existente:
                return HttpResponse(f'Ya existe este proveedor.')
            else:
                proveedor = Proveedor(empresa=empresa, direccion=direccion, telefono=telefono)
                proveedor.save()
                return render(req, 'inicio.html')
    else:
        miFormulario = ProveedorFormulario()
    return render(req, 'proveedorFormulario.html', {"miFormulario": miFormulario})
    
def busquedaProveedor(req):
    return render(req, 'busquedaProveedor.html')

def buscarProveedor(request):
    consulta = request.GET.get('consulta', '')

    if consulta:
        proveedores = Proveedor.objects.filter(
            Q(empresa__icontains=consulta) |
            Q(direccion__icontains=consulta) | 
            Q(telefono__icontains=consulta) 
        )
        return render(request, 'resultadosBusqueda.html', {"resultados": proveedores, "modelo": "Proveedor"})
    else:
        mensaje_error = "Por favor, ingresa un término de búsqueda para buscar proveedores."
        return render(request, 'errorBusqueda.html', {"mensaje_error": mensaje_error})
