from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Carrito_item)
admin.site.register(Compras)
admin.site.register(Compras_Item)
admin.site.register(Pedidos)
admin.site.register(Subscripcion)