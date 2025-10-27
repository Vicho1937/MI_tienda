===========================================
 PROYECTO: MI_TIENDA (Control de Ventas)
===========================================

Este proyecto es una aplicación web hecha con Django para llevar el control
de productos, clientes y ventas.

-------------------------------------------
REQUERIMIENTOS CUBIERTOS
-------------------------------------------
1. Registrar productos con nombre, código, cantidad y precio.
2. Listar productos disponibles.
3. Editar productos y actualizar su stock.
4. Eliminar productos.
5. Registrar ventas asignadas a un cliente (por RUT).
6. Guardar datos del cliente si desea ser habitual.
7. En caso de no ser habitual, solo se pide el RUT para la boleta.

-------------------------------------------
ESTRUCTURA DEL PROYECTO
-------------------------------------------

MI_tienda/                 <- Carpeta principal
│
├── manage.py              <- Script principal para ejecutar comandos Django
│
├── tienda/                <- Configuración global del proyecto
│   ├── settings.py        <- Configuración principal del proyecto
│   ├── urls.py            <- Rutas principales
│   ├── asgi.py / wsgi.py  <- Archivos para despliegue
│   └── __init__.py
│
├── ventas/                <- Aplicación principal de control de ventas
│   ├── models.py          <- Modelos (tablas de la BD: Cliente, Producto, Venta)
│   ├── views.py           <- Lógica de negocio y controladores
│   ├── forms.py           <- Formularios de Django para Producto, Cliente, Venta
│   ├── urls.py            <- Rutas específicas de la app
│   ├── admin.py           <- Registro de modelos en el panel de administración
│   ├── apps.py            <- Configuración de la app
│   ├── migrations/        <- Historial de cambios de base de datos
│   └── __init__.py
│
├── templates/             <- Plantillas HTML
│   ├── eliminar_producto.html<- Confirmación para borrar producto
│   ├── form_producto.html    <- Formulario para crear/editar producto
│   ├── form_venta.html       <- Formulario para registrar ventas
│   ├── lista_productos.html  <- Lista de productos disponibles
└────── base.html             <- Plantilla base (estructura común)

-------------------------------------------
COMANDOS BÁSICOS
-------------------------------------------
1. Iniciar servidor de desarrollo:
   python manage.py runserver

2. Crear migraciones cuando cambien los modelos:
   python manage.py makemigrations
   python manage.py migrate

3. Crear superusuario para entrar al admin:
   python manage.py createsuperuser

-------------------------------------------
NOTAS
-------------------------------------------
- El proyecto usa Tailwind CSS para el diseño de las plantillas.
- Los templates personalizados de "ventas" son los que ve el usuario final.
- El panel de administración se usa tal como viene por defecto en Django.