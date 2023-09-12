# ALUMNO AGUSTIN LUCAS PONCE DE LEON
# PROYECTO PYTHON - CURSO CODER HOUSE

from django import forms
from .models import Pedido, Proveedor

class ProductoFormulario(forms.Form):
    producto = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=20)
    talle = forms.CharField()
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

class PedidoFormulario(forms.Form):
    cliente = forms.CharField(max_length=40)
    productos = forms.CharField(max_length=40)
    fecha_pedido = forms.DateField()

    class Meta:
        model = Pedido
        fields = ['cliente', 'productos', 'fecha_pedido']

class ProveedorFormulario(forms.Form):
    empresa = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=15)