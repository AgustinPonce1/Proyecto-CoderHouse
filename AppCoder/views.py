# ALUMNO AGUSTIN LUCAS PONCE DE LEON
# PROYECTO PYTHON - CURSO CODER HOUSE

from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.http import HttpResponse
from .forms import *
from django.db.models import Q #Añadi esta clase para los formularios y realizar las busquedas de filtro más complejas y flexibles
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def producto(req, nombre, marca):
    producto = Producto(nombre=nombre, marca=marca)
    producto.save()
    return HttpResponse(f"""
    <p>Producto: {producto.nombre} - Marca: {producto.marca} creado con éxito!</p>
    """)

def listar_productos(request):

    productos = Producto.objects.all()
    
    return render(request, 'lista_productos.html', {"lista_productos": productos})

def inicio(req):
    return render(req, 'inicio.html')

def detalle_producto(request, producto_id):

    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def marcas(request):
    return render(request, 'marcas.html')


def SobreMi(request):
    return render(request, 'SobreMi.html')

def contacto(request):
    return render(request, 'contacto.html')

#FORMULARIO CLASE PRODUCTO
def productoFormulario(req):
    if req.method == 'POST':
        miFormulario = ProductoFormulario(req.POST, req.FILES)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            nombre = data['nombre']
            marca = data['marca']
            talle = data['talle']
            precio = data['precio']
            producto_existente = Producto.objects.filter(nombre=nombre, marca=marca, talle=talle, precio=precio).first()
            if producto_existente:
                return HttpResponse(f'Ya existe este producto!')
            else:
                imagen = data.get('imagen')
                producto = Producto(nombre=nombre, marca=marca, talle=talle, precio=precio, imagen=imagen) 
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
            return render(req, 'inicio.html')  # O redirige a donde desees, tambien se puede usar redirect

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
    
#LogIn de usuarios
def loginView(req):

    if req.method == 'POST':
        miFormulario = AuthenticationForm(req, data=req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data['username']
            psw = data['password']

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)

                return render(req, 'inicio.html', {"mensaje": f'Bienvenido {usuario}'})

        return render(req, 'inicio.html', {"mensaje": f'Datos Incorrectos'})
    else:
        miFormulario = AuthenticationForm()
        return render(req, 'login.html', {"miFormulario": miFormulario})

#Registro de usuarios
def register(req):
    if req.method == 'POST':
        miFormulario = CustomUserCreationForm(data=req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data['username']
            miFormulario.save()
            return render(req, 'inicio.html', {"mensaje": f'Usuario {usuario} creado con éxito'})
        return render(req, 'inicio.html', {"mensaje": f'Formulario Inválido'})
    else:
        miFormulario = CustomUserCreationForm()
        return render(req, 'registro.html', {"miFormulario": miFormulario})


def agregar_avatar(req):

    if req.method == 'POST':
        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            avatar = Avatar(user=req.user, imagen=data["imagen"])
            avatar.save()
            return render(req, 'inicio.html', {"mensaje": f'Avatar actualizado con éxito!', "url_avatar": avatar.imagen.url})
            
        return render(req, 'inicio.html', {"mensaje": f'Formulario Inválido'})
    else:
        miFormulario = AvatarFormulario()
        return render(req, 'agregarAvatar.html', {"miFormulario": miFormulario})

def user_view(request):
    return render(request, 'usuarios.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('first_name')
        user.email = request.POST.get('email')
        user.description = request.POST.get('description') 
        user.website = request.POST.get('website')  
        user.save()
        return render(request, 'usuarios.html', {'user': request.user})
    return render(request, 'edit_profile.html', {'user': request.user})

@login_required
def change_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
        else:
            user = request.user
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)

            messages.success(request, 'La contraseña se cambió correctamente.')
            return render(request, 'usuarios.html', {'user': request.user})

    return render(request, 'change_password.html')

def es_administrador(user):
    return user.is_authenticated and user.is_staff 

# Editar producto
@user_passes_test(es_administrador)
def editar_producto(request, pk):

    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('ListaProductos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

# Eliminar producto
@user_passes_test(es_administrador)
def eliminar_producto(request, pk):

    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('ListaProductos')
    
    return render(request, 'eliminar_producto.html', {'producto': producto})

@login_required
def vista_de_mensajes(request):
    try:
        mensajes_enviados = Mensaje.objects.filter(remitente=request.user)
        mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)

        if request.method == 'POST':
            formulario = MensajeForm(request.POST)
            if formulario.is_valid():
                mensaje = formulario.save(commit=False)
                mensaje.remitente = request.user
                mensaje.save()
                return redirect('vista_de_mensajes')
        else:
            formulario = MensajeForm()

        return render(request, 'mensajes.html', {
            'mensajes_enviados': mensajes_enviados,
            'mensajes_recibidos': mensajes_recibidos,
            'formulario': formulario
        })
    except ObjectDoesNotExist:
        mensaje_error = "No se encontraron mensajes o hubo un error al cargarlos."
        return render(request, 'error.html', {'mensaje_error': mensaje_error})
    
