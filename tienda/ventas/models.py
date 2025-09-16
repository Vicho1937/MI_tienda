from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100, blank=True)
    habitual = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.rut} - {self.nombre or 'Cliente ocasional'}"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    cliente_rut = models.CharField("RUT (si no es cliente registrado)", max_length=12, blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.cantidad * self.producto.precio

    def __str__(self):
        rut = self.cliente.rut if self.cliente else (self.cliente_rut or "Sin RUT")
        return f"Venta {self.id} - {rut} - {self.producto.nombre} x{self.cantidad}"
