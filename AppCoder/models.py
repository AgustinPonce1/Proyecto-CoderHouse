# ALUMNO AGUSTIN LUCAS PONCE DE LEON
# PROYECTO PYTHON - CURSO CODER HOUSE

from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    fecha_creacion = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    talle = models.CharField(max_length=1000, blank=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.marca}'
    
    class Meta():

        verbose_name = 'Producto' #Nombre en caso individual
        verbose_name_plural = 'Productos' #Nombre para casos plurales
        ordering = ('nombre', '-marca') #Ordenar alfabeticamente

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    fecha_pedido = models.DateField()

    def __str__(self):
        productos_str = ', '.join(str(producto) for producto in self.productos.all())
        return f'{self.cliente} - {productos_str}'
        

class Proveedor(models.Model):
    empresa = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    productos = models.ManyToManyField(Producto)

    def __str__(self):
        productos_str = ', '.join(str(producto) for producto in self.productos.all())
        return f'{self.empresa} - {productos_str}'
    
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', blank=True, null=True)

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensajes_recibidos', on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    groups = models.ManyToManyField('auth.Group', related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_users', blank=True)

    def __str__(self):
        return self.username
