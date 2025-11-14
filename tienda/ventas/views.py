from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import ProtectedError, Sum, Count
from django.http import HttpResponse
from django.utils import timezone
from rest_framework import viewsets, permissions
from .models import Producto, Cliente, Venta
from .forms import ProductoForm, VentaForm
from .serializers import ProductoSerializer
import csv

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
        try:
            nombre_producto = producto.nombre
            producto.delete()
            messages.success(request, f"Producto '{nombre_producto}' eliminado correctamente.")
            return redirect('ventas:lista_productos')
        except ProtectedError:
            messages.error(
                request, 
                f"No se puede eliminar '{producto.nombre}' porque tiene ventas registradas. "
                "Elimina primero las ventas asociadas o cambia el stock a 0."
            )
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

def lista_ventas(request):
    """Lista de ventas con filtros y opción de exportar"""
    ventas = Venta.objects.all().select_related('cliente', 'producto').order_by('-fecha')
    
    # Filtros
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')
    producto_id = request.GET.get('producto')
    cliente_id = request.GET.get('cliente')
    
    if fecha_desde:
        ventas = ventas.filter(fecha__date__gte=fecha_desde)
    if fecha_hasta:
        ventas = ventas.filter(fecha__date__lte=fecha_hasta)
    if producto_id:
        ventas = ventas.filter(producto_id=producto_id)
    if cliente_id:
        ventas = ventas.filter(cliente_id=cliente_id)
    
    # Estadísticas
    total_ventas = ventas.aggregate(
        total_cantidad=Sum('cantidad'),
        num_ventas=Count('id')
    )
    
    total_monto = sum(venta.total() for venta in ventas)
    
    context = {
        'ventas': ventas,
        'productos': Producto.objects.all(),
        'clientes': Cliente.objects.filter(habitual=True),
        'total_cantidad': total_ventas['total_cantidad'] or 0,
        'num_ventas': total_ventas['num_ventas'] or 0,
        'total_monto': total_monto,
        'fecha_desde': fecha_desde,
        'fecha_hasta': fecha_hasta,
        'producto_id': producto_id,
        'cliente_id': cliente_id,
    }
    
    return render(request, 'ventas/lista_ventas.html', context)

def exportar_ventas_csv(request):
    """Exportar ventas filtradas a CSV para Excel"""
    ventas = Venta.objects.all().select_related('cliente', 'producto').order_by('-fecha')
    
    # Aplicar los mismos filtros que en lista_ventas
    fecha_desde = request.GET.get('fecha_desde')
    fecha_hasta = request.GET.get('fecha_hasta')
    producto_id = request.GET.get('producto')
    cliente_id = request.GET.get('cliente')
    
    if fecha_desde:
        ventas = ventas.filter(fecha__date__gte=fecha_desde)
    if fecha_hasta:
        ventas = ventas.filter(fecha__date__lte=fecha_hasta)
    if producto_id:
        ventas = ventas.filter(producto_id=producto_id)
    if cliente_id:
        ventas = ventas.filter(cliente_id=cliente_id)
    
    # Crear respuesta CSV
    response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
    response['Content-Disposition'] = f'attachment; filename="ventas_{timezone.now().strftime("%Y%m%d_%H%M%S")}.csv"'
    
    # BOM para que Excel abra correctamente con tildes y ñ
    response.write('\ufeff')
    
    writer = csv.writer(response, delimiter=';', quoting=csv.QUOTE_ALL)
    
    # Encabezados con formato profesional
    writer.writerow([
        'ID Venta',
        'Fecha',
        'Hora',
        'Cliente',
        'RUT Cliente',
        'Tipo Cliente',
        'Producto',
        'Código Producto',
        'Cantidad',
        'Precio Unitario (CLP)',
        'Total Venta (CLP)',
    ])
    
    # Datos de ventas
    total_general = 0
    total_cantidad = 0
    
    for venta in ventas:
        # Información del cliente
        if venta.cliente:
            cliente_nombre = venta.cliente.nombre or 'Sin nombre'
            cliente_rut = venta.cliente.rut
            tipo_cliente = 'Habitual' if venta.cliente.habitual else 'Registrado'
        else:
            cliente_nombre = 'Cliente Ocasional'
            cliente_rut = venta.cliente_rut or 'Sin RUT'
            tipo_cliente = 'Ocasional'
        
        # Formatear fecha y hora
        fecha_str = venta.fecha.strftime('%d/%m/%Y')
        hora_str = venta.fecha.strftime('%H:%M:%S')
        
        # Calcular total
        total = venta.total()
        total_general += total
        total_cantidad += venta.cantidad
        
        writer.writerow([
            venta.id,
            fecha_str,
            hora_str,
            cliente_nombre,
            cliente_rut,
            tipo_cliente,
            venta.producto.nombre,
            venta.producto.codigo,
            venta.cantidad,
            f"{venta.producto.precio:,.0f}",
            f"{total:,.0f}",
        ])
    
    # Fila de totales
    writer.writerow([])
    writer.writerow([
        'TOTALES',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        total_cantidad,
        '',
        f"{total_general:,.0f}",
    ])
    
    # Información adicional
    writer.writerow([])
    writer.writerow(['Reporte generado:', timezone.now().strftime('%d/%m/%Y %H:%M:%S')])
    writer.writerow(['Total de ventas:', ventas.count()])
    writer.writerow(['Monto total:', f"${total_general:,.0f}"])
    
    return response

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by("nombre")
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]
