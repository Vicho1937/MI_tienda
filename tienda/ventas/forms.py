from django import forms
from .models import Producto, Cliente, Venta
import re

RUT_REGEX = re.compile(r'^[0-9Kk\-]{7,12}$')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'cantidad', 'precio']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'habitual']

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not RUT_REGEX.match(rut):
            raise forms.ValidationError("RUT inválido (ej: 12345678-9)")
        return rut


class VentaForm(forms.ModelForm):
    cliente_rut = forms.CharField(required=False, label="RUT ocasional")
    nombre_cliente = forms.CharField(required=False, label="Nombre cliente")
    guardar_cliente = forms.BooleanField(required=False, label="Guardar como habitual")

    class Meta:
        model = Venta
        fields = ['cliente', 'cliente_rut', 'nombre_cliente', 'guardar_cliente', 'producto', 'cantidad']

    def clean(self):
        cleaned = super().clean()
        cliente = cleaned.get('cliente')
        cliente_rut = cleaned.get('cliente_rut')
        producto = cleaned.get('producto')
        cantidad = cleaned.get('cantidad')

        if not cliente and not cliente_rut:
            raise forms.ValidationError("Debe ingresar cliente habitual o un RUT ocasional.")

        if producto and cantidad:
            if cantidad <= 0:
                raise forms.ValidationError("La cantidad debe ser mayor que 0.")
            if cantidad > producto.cantidad:
                raise forms.ValidationError(f"Stock insuficiente ({producto.cantidad} disponibles).")

        return cleaned
