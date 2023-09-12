# ALUMNO AGUSTIN LUCAS PONCE DE LEON
# PROYECTO PYTHON - CURSO CODER HOUSE

from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    fecha_creacion = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True) 
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    talle = models.CharField(max_length=1000, blank=True)

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