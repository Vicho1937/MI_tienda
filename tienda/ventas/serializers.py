from rest_framework import serializers
from .models import Producto, Cliente, Venta

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VentaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    total = serializers.SerializerMethodField()
    
    class Meta:
        model = Venta
        fields = '__all__'
    
    def get_total(self, obj):
        return obj.total()
