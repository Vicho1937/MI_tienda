# 🛒 Sistema de Ventas - MI_tienda

Sistema de gestión de ventas desarrollado con Django y PostgreSQL (Supabase).

## 🚀 Instalación

### 1. Instalar dependencias

```bash
pip install django python-dotenv psycopg2-binary
```

### 2. Configurar variables de entorno

Copia el archivo `.env.example` y renómbralo a `.env`, luego completa con tus datos de Supabase:

```env
user=postgres.xxxxxxxxxxxxx
password=tu_password_aqui
host=aws-1-us-east-2.pooler.supabase.com
port=6543
dbname=postgres
```

### 3. Probar conexión (Opcional)

```bash
python test_connection.py
```

### 4. Ejecutar el proyecto

**Opción 1: Doble clic en el archivo**
```
run_supabase.bat
```

**Opción 2: Desde CMD**
```bash
cd MI_tienda
run_supabase.bat
```

## 📋 Características

✅ Gestión de productos con validaciones
- Código único (2-20 caracteres)
- Stock (0-999,999 unidades)
- Precio con validación (mayor a 0)

✅ Registro de ventas
- Clientes habituales u ocasionales
- Validación de RUT chileno
- Control de stock automático

✅ Interfaz moderna con TailwindCSS
- Indicadores visuales de stock
- Validaciones en tiempo real
- Responsive design

✅ Base de datos PostgreSQL en Supabase
- Conexión segura con SSL
- Variables de entorno para datos sensibles

## 🔒 Seguridad

- Archivo `.env` no se sube a git (incluido en .gitignore)
- Contraseñas y datos sensibles en variables de entorno
- Validaciones en frontend y backend

## 🛠️ Tecnologías

- Django 4.x
- PostgreSQL (Supabase)
- TailwindCSS
- Python 3.x
- python-dotenv
- psycopg2

## 📝 Notas

- Los productos con ventas registradas están protegidos contra eliminación
- Los códigos de productos se convierten automáticamente a mayúsculas
- El sistema valida formato de RUT chileno (12345678-9)
