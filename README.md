# 🛒 Sistema de Ventas con Supabase

## 🚀 Inicio Rápido

### 1. Instalar dependencias (solo la primera vez)
```bash
pip install django python-dotenv psycopg2-binary
```

### 2. Ejecutar el servidor

**Forma más simple:**
```bash
cd tienda
python manage.py runserver
```

Si es la primera vez, ejecuta antes:
```bash
cd tienda
python manage.py migrate
python manage.py runserver
```

### 3. Abrir en el navegador
```
http://127.0.0.1:8000
```

## 📝 Base de Datos

✅ **Ya está configurado con Supabase PostgreSQL**

El archivo `.env` contiene las credenciales.

## 🎯 Comandos Principales

```bash
# SIEMPRE desde la carpeta tienda/
cd tienda

# Iniciar servidor
python manage.py runserver

# Aplicar cambios de base de datos (primera vez)
python manage.py migrate

# Crear admin
python manage.py createsuperuser
```

## 🛠️ Tecnologías

- Django + PostgreSQL (Supabase)
- TailwindCSS
- Python 3.12
