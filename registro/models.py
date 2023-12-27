from django.db import models
# en models.py
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    # Agrega campos adicionales si es necesario

    # Agrega related_name a la relación con grupos
    groups = models.ManyToManyField(Group, related_name='usuarios_groups')

    # Agrega related_name a la relación con permisos
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_permissions')

    class Meta:
        permissions = [
            ("can_do_something", "Puede hacer algo"),
        ]
# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidop = models.CharField(max_length=100)
    apellidom = models.CharField(max_length=100)
    direccion = models.CharField(max_length= 250)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre


    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)


    def __str__(self):
        return self.nombre
    
class Pedido(models.Model):
    fecha_creacion = models.DateField()
    estado_pedido = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('completado', 'Completado'), ('cancelado', 'Cancelado')])
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"
    

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"Detalle {self.id} - Pedido {self.pedido.id}, Producto {self.producto.nombre}"
    
class RegistroVentas(models.Model):
    fecha_venta = models.DateField()
    total_ventas = models.DecimalField(max_digits=12, decimal_places=2)
    pedidos = models.ManyToManyField(Pedido)

    def __str__(self):
        return f"Venta {self.id} - Total: {self.total_ventas}"
    

