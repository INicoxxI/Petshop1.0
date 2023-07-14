from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    descripcion = models.CharField(max_length=200, null=False)

    def __str__(self) -> str:
        return f"Id: {self.id} | Descripcion: {self.descripcion}"


class Producto(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id de producto')
    titulo = models.CharField(max_length=50, null=False)
    stock = models.IntegerField(default=1)
    imagen = models.FileField(upload_to='img')
    descripcion = models.CharField(max_length=200, null=False)
    precio = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, related_name="productos")

    def __str__(self) -> str:
        return f"Id: {self.id} | Titulo: {self.titulo} |  Stock: {self.stock} | Imagen: {self.imagen} | Descripcion: {self.descripcion} | Precio: {self.precio} || Categoria_id: {self.categoria.id} "


class Carrito(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id de carrito')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carrito")
    total = models.DecimalField(null=False, max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Id: {self.id} | Usuario_id: {self.usuario.id} | Usuario: {self.usuario.username} | Total: {self.total}"


class Carrito_item(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id de Item carrito')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")

    def __str__(self) -> str:
        return f"Id: {self.id} | Producto: {self.producto.titulo} | Carrito_id: {self.carrito.id}"

class Compras(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="compras")
    total = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, null=False)

    def __str__(self) -> str:
        return f"Id: {self.pk} | Usuario_id: {self.usuario.id} | Usuario: {self.usuario.username} | total: {self.total} | Estado: {self.estado}" 

class Compras_Item(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    compras = models.ForeignKey(Compras, on_delete=models.CASCADE, related_name="items_compra")
  

    def __str__(self) -> str:
        return f"Id: {self.pk} | Producto: {self.producto.titulo} | Compras_id: {self.compra.id} " 



class Pedidos(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id de Pedidos')
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="carrito_pedidos")
    estado = models.IntegerField( verbose_name='Estado_Pedido')

    def __str__(self) -> str:
        return f"Id: {self.id} | carrito {self.carrito} | estado: {self.estado} "


class Subscripcion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,related_name="subscripcion")
    vigente = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Id: {self.pk} | Usuario_id: {self.usuario.id} | Usuario: {self.usuario.username} | Vigente: {self.vigente}"
