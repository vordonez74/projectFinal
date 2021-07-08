from django.db import models

# Create your models here.


class Categorias(models.Model):
    descripcion = models.CharField(max_length=64)

    def __str__(self):
        return f"id #{self.id} desc. {self.descripcion}"


class Productos(models.Model):
    titulo = models.CharField(max_length=64)
    Imagen = models.CharField(max_length=64)
    descripcion = models.CharField(max_length=64)
    precio = models.CharField(max_length=64)
    Categorias = models.ForeignKey(
        Categorias, on_delete=models.CASCADE, related_name="catogory")

    def __str__(self):
        return f"{self.titulo} - {self.descripcion} - precio {self.precio}"


class Carrito(models.Model):
    usuario = models.CharField(max_length=64)
    listaProductos = models.ManyToManyField(
        Productos, blank=True, related_name="Carritos")
    totalCarrito = models.FloatField()

    def __str__(self):
        return f"{self.usuario} total {self.totalCarrito}"
