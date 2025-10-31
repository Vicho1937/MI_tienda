from django import forms
from .models import Producto, Cliente, Venta
import re

RUT_REGEX = re.compile(r'^[0-9Kk\-]{7,12}$')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'codigo', 'cantidad', 'precio']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Ej: Coca Cola 500ml',
                'maxlength': '100'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Ej: PROD001',
                'maxlength': '20'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Stock disponible',
                'min': '0',
                'max': '999999'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.01'
            }),
        }
    
    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if codigo:
            codigo = codigo.strip().upper()
            if len(codigo) < 2:
                raise forms.ValidationError("El código debe tener al menos 2 caracteres.")
        return codigo
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio and precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor a 0.")
        return precio
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad is not None and cantidad < 0:
            raise forms.ValidationError("La cantidad no puede ser negativa.")
        if cantidad and cantidad > 999999:
            raise forms.ValidationError("La cantidad máxima es 999,999 unidades.")
        return cantidad


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'habitual']
        widgets = {
            'rut': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Ej: 12345678-9',
                'maxlength': '12',
                'pattern': '[0-9]{7,8}-[0-9Kk]'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Nombre del cliente',
                'maxlength': '100'
            }),
            'habitual': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'
            })
        }

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not RUT_REGEX.match(rut):
            raise forms.ValidationError("RUT inválido. Formato esperado: 12345678-9")
        return rut.upper()


class VentaForm(forms.ModelForm):
    cliente_rut = forms.CharField(
        required=False, 
        label="RUT ocasional",
        max_length=12,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Ej: 12345678-9',
            'maxlength': '12',
            'pattern': '[0-9]{7,8}-[0-9Kk]',
            'title': 'Formato: 12345678-9'
        })
    )
    nombre_cliente = forms.CharField(
        required=False, 
        label="Nombre cliente",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Nombre del cliente',
            'maxlength': '100',
            'pattern': '[A-Za-zÁÉÍÓÚáéíóúÑñ ]+',
            'title': 'Solo letras y espacios'
        })
    )
    guardar_cliente = forms.BooleanField(
        required=False, 
        label="Guardar como habitual",
        widget=forms.CheckboxInput(attrs={
            'class': 'h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'
        })
    )

    class Meta:
        model = Venta
        fields = ['cliente', 'cliente_rut', 'nombre_cliente', 'guardar_cliente', 'producto', 'cantidad']
        widgets = {
            'cliente': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'producto': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'cantidad': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Cantidad a vender',
                'min': '1'
            }),
        }

    def clean(self):
        cleaned = super().clean()
        cliente = cleaned.get('cliente')
        cliente_rut = cleaned.get('cliente_rut')
        nombre_cliente = cleaned.get('nombre_cliente')
        producto = cleaned.get('producto')
        cantidad = cleaned.get('cantidad')

        if not cliente and not cliente_rut:
            raise forms.ValidationError("Debe ingresar cliente habitual o un RUT ocasional.")
        
        if cliente_rut:
            cliente_rut = cliente_rut.strip()
            if not RUT_REGEX.match(cliente_rut):
                raise forms.ValidationError("El RUT ingresado no es válido. Formato esperado: 12345678-9")
            cleaned['cliente_rut'] = cliente_rut.upper()
        
        if nombre_cliente:
            nombre_cliente = nombre_cliente.strip()
            if not nombre_cliente.replace(' ', '').isalpha():
                raise forms.ValidationError("El nombre solo puede contener letras y espacios.")
            cleaned['nombre_cliente'] = nombre_cliente.title()

        if producto and cantidad:
            if cantidad <= 0:
                raise forms.ValidationError("La cantidad debe ser mayor que 0.")
            if cantidad > producto.cantidad:
                raise forms.ValidationError(f"Stock insuficiente. Solo hay {producto.cantidad} unidades disponibles.")

        return cleaned
