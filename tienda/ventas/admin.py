from django.contrib import admin
from .models import Cliente, Producto, Venta

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'habitual')
    search_fields = ('rut', 'nombre')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'cantidad', 'precio')
    search_fields = ('nombre', 'codigo')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'cliente_rut', 'producto', 'cantidad', 'fecha')
    list_filter = ('fecha',)
