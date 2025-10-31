# 📊 Exportación de Ventas a CSV/Excel

## ✅ Características Implementadas

### 1️⃣ **Desde el Panel de Admin Django**

Accede a: `http://127.0.0.1:8000/admin/ventas/venta/`

**Opciones disponibles:**
- ✅ Selecciona ventas específicas y exporta
- ✅ Exporta TODAS las ventas con un clic
- ✅ Archivo CSV optimizado para Excel (con separador `;` y encoding UTF-8-sig)

**Cómo usar:**
1. Inicia sesión en el admin
2. Ve a "Ventas" 
3. Selecciona las ventas que quieres exportar
4. En el menú "Acción", elige:
   - `📊 Exportar a CSV (Excel)` → Exporta las seleccionadas
   - `📊 Exportar TODAS las ventas a CSV` → Exporta todo

### 2️⃣ **Desde la Interfaz Web (Con Filtros)**

Accede a: `http://127.0.0.1:8000/ventas/lista/`

**Características:**
- ✅ Filtrar por fecha (desde/hasta)
- ✅ Filtrar por producto
- ✅ Filtrar por cliente
- ✅ Ver estadísticas en tiempo real
- ✅ Exportar ventas filtradas con un clic

**Cómo usar:**
1. Navega a "📊 Ventas" en el menú
2. Aplica los filtros que necesites
3. Click en "📥 Exportar a CSV/Excel"

## 📄 Formato del CSV

El archivo incluye las siguientes columnas:

```
ID Venta | Fecha | Hora | Cliente | RUT Cliente | Tipo Cliente | 
Producto | Código Producto | Cantidad | Precio Unitario | Total Venta
```

**Plus:** Al final del archivo se incluye:
- 📊 Totales de cantidad y monto
- 📅 Fecha de generación del reporte
- 🔢 Número total de ventas

## 🔧 Características Técnicas

- ✅ **Formato Excel-friendly**: Usa separador `;` (punto y coma)
- ✅ **Encoding UTF-8-sig**: Soporte completo para tildes, ñ y caracteres especiales
- ✅ **BOM para Excel**: Se abre correctamente en Excel sin configuración
- ✅ **Formato CLP**: Precios formateados con separador de miles
- ✅ **Tuplas organizadas**: Cada fila es una venta completa

## 📂 Ubicación de Archivos

Los CSV se descargan con nombre:
```
ventas_YYYYMMDD_HHMMSS.csv
```

Ejemplo: `ventas_20251031_163000.csv`

## 🚀 Inicio Rápido

```bash
# 1. Crear un superusuario si no existe
cd tienda
python manage.py createsuperuser

# 2. Iniciar servidor
python manage.py runserver

# 3. Acceder:
# - Admin: http://127.0.0.1:8000/admin/
# - Lista de Ventas: http://127.0.0.1:8000/ventas/lista/
```

## 📝 Ejemplo de Uso

### Exportar ventas del mes actual:
1. Ve a "📊 Ventas"
2. Fecha desde: `01/10/2025`
3. Fecha hasta: `31/10/2025`
4. Click en "📥 Exportar a CSV/Excel"
5. Abre el archivo en Excel → Listo! ✅

### Exportar ventas de un producto específico:
1. Ve a "📊 Ventas"
2. Selecciona el producto en el filtro
3. Click en "📥 Exportar a CSV/Excel"

## ⚠️ Nota Importante

El archivo CSV usa **punto y coma (`;`)** como separador para compatibilidad con Excel en español. Si usas Excel en inglés, puede que necesites cambiar el separador en la configuración regional.
