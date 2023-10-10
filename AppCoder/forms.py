# ALUMNO AGUSTIN LUCAS PONCE DE LEON
# PROYECTO PYTHON - CURSO CODER HOUSE

from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    marca = forms.CharField(max_length=40)
    talle = forms.CharField()
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    imagen = forms.ImageField(required=False)

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

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ("imagen",)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'marca', 'talle', 'precio', 'imagen']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False, help_text='Opcional. Introduce tu dirección de correo electrónico.')
    description = forms.CharField(widget=forms.Textarea, required=False, label='Descripción', max_length=500)
    website = forms.URLField(required=False, label='Enlace a la página web')

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'description', 'website')

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']