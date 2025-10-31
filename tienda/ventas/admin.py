from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone
import csv
from .models import Cliente, Producto, Venta

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'habitual')
    search_fields = ('rut', 'nombre')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'cantidad', 'precio')
    search_fields = ('nombre', 'codigo')

def exportar_ventas_csv(modeladmin, request, queryset):
    """Exportar ventas seleccionadas a CSV para Excel"""
    response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
    response['Content-Disposition'] = f'attachment; filename="ventas_{timezone.now().strftime("%Y%m%d_%H%M%S")}.csv"'
    
    # Usar utf-8-sig para que Excel abra correctamente con tildes
    response.write('\ufeff')  # BOM para Excel
    
    writer = csv.writer(response, delimiter=';', quoting=csv.QUOTE_ALL)
    
    # Encabezados
    writer.writerow([
        'ID Venta',
        'Fecha',
        'Hora',
        'Cliente',
        'RUT Cliente',
        'Producto',
        'Código Producto',
        'Cantidad',
        'Precio Unitario',
        'Total',
        'Tipo Cliente'
    ])
    
    # Datos
    for venta in queryset.order_by('-fecha'):
        # Obtener información del cliente
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
        
        writer.writerow([
            venta.id,
            fecha_str,
            hora_str,
            cliente_nombre,
            cliente_rut,
            venta.producto.nombre,
            venta.producto.codigo,
            venta.cantidad,
            f"${venta.producto.precio:,.0f}",
            f"${total:,.0f}",
            tipo_cliente
        ])
    
    return response

exportar_ventas_csv.short_description = "📊 Exportar a CSV (Excel)"

def exportar_todas_ventas_csv(modeladmin, request, queryset):
    """Exportar TODAS las ventas a CSV (ignora selección)"""
    todas_ventas = Venta.objects.all()
    return exportar_ventas_csv(modeladmin, request, todas_ventas)

exportar_todas_ventas_csv.short_description = "📊 Exportar TODAS las ventas a CSV"

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_cliente_display', 'producto', 'cantidad', 'get_total', 'fecha')
    list_filter = ('fecha', 'producto')
    search_fields = ('cliente__rut', 'cliente__nombre', 'cliente_rut', 'producto__nombre')
    date_hierarchy = 'fecha'
    actions = [exportar_ventas_csv, exportar_todas_ventas_csv]
    
    def get_cliente_display(self, obj):
        if obj.cliente:
            return f"{obj.cliente.nombre or 'Sin nombre'} ({obj.cliente.rut})"
        return f"Ocasional ({obj.cliente_rut or 'Sin RUT'})"
    get_cliente_display.short_description = 'Cliente'
    
    def get_total(self, obj):
        return f"${obj.total():,.0f}"
    get_total.short_description = 'Total'
    get_total.admin_order_field = 'producto__precio'
