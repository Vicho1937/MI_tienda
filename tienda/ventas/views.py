from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Producto, Cliente, Venta
from .forms import ProductoForm, VentaForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/lista_productos.html', {'productos': productos})

def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado correctamente.")
            return redirect('ventas:lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'ventas/form_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado.")
            return redirect('ventas:lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'ventas/form_producto.html', {'form': form})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, "Producto eliminado.")
        return redirect('ventas:lista_productos')
    return render(request, 'ventas/eliminar_producto.html', {'producto': producto})

def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data.get('cliente')
            cliente_rut = form.cleaned_data.get('cliente_rut')
            nombre_cliente = form.cleaned_data.get('nombre_cliente')
            guardar_cliente = form.cleaned_data.get('guardar_cliente')
            producto = form.cleaned_data['producto']
            cantidad = form.cleaned_data['cantidad']

            if cliente:
                venta = Venta.objects.create(cliente=cliente, producto=producto, cantidad=cantidad)
            else:
                if guardar_cliente:
                    cliente, _ = Cliente.objects.get_or_create(
                        rut=cliente_rut,
                        defaults={'nombre': nombre_cliente, 'habitual': True}
                    )
                    venta = Venta.objects.create(cliente=cliente, producto=producto, cantidad=cantidad)
                else:
                    venta = Venta.objects.create(cliente=None, cliente_rut=cliente_rut, producto=producto, cantidad=cantidad)

            producto.cantidad -= cantidad
            producto.save()
            messages.success(request, f"Venta registrada. Total: ${venta.total():.0f}")
            return redirect('ventas:lista_productos')
    else:
        form = VentaForm()
    return render(request, 'ventas/form_venta.html', {'form': form})
