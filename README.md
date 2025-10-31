# 🛒 Sistema de Ventas con Supabase

## 🌐 EN PRODUCCIÓN

**URL:** https://mitienda-production.up.railway.app

---

## 🚀 Inicio Rápido (Desarrollo Local)

### 1. Instalar dependencias (solo la primera vez)
```bash
pip install -r requirements.txt
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

---

## 🚢 Despliegue en Railway

Ver documentación completa: **[RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md)**

### Variables de entorno necesarias:
Ver: **[VARIABLES_RAILWAY.txt](VARIABLES_RAILWAY.txt)**

### Deploy rápido:
```bash
# Opción 1: Script automático
deploy.bat

# Opción 2: Manual
git add .
git commit -m "Actualización"
git push origin main
```

---

## 📝 Base de Datos

✅ **PostgreSQL en Supabase**

El archivo `.env` contiene las credenciales (desarrollo).  
En Railway, las variables se configuran en el panel.

---

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

# Recolectar archivos estáticos (producción)
python manage.py collectstatic
```

---

## 📊 Características

- ✅ Gestión de productos con validaciones
- ✅ Registro de ventas (clientes habituales/ocasionales)
- ✅ Exportación CSV/Excel con filtros
- ✅ Panel de administración Django
- ✅ Base de datos PostgreSQL (Supabase)
- ✅ Interfaz moderna con TailwindCSS
- ✅ Desplegado en Railway (Producción)

---

## 🛠️ Stack Tecnológico

- **Backend:** Django 5.1.2
- **Base de Datos:** PostgreSQL (Supabase)
- **Frontend:** TailwindCSS
- **Servidor:** Gunicorn
- **Archivos Estáticos:** WhiteNoise
- **Hosting:** Railway
- **Python:** 3.12

---

## 📁 Estructura del Proyecto

```
MI_tienda/
├── tienda/
│   ├── manage.py
│   ├── tienda/          # Configuración Django
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── ventas/          # App principal
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│       ├── admin.py
│       └── templates/
├── .env                 # Variables locales (no subir a git)
├── requirements.txt     # Dependencias Python
├── Procfile            # Configuración Railway
├── railway.json        # Configuración Railway
└── runtime.txt         # Versión Python
```

---

## 🔒 Seguridad

- Variables de entorno para credenciales
- DEBUG=False en producción
- HTTPS automático en Railway
- CSRF protection habilitado
- Conexión SSL a Supabase

---

## 📚 Documentación Adicional

- **[EXPORTACION_CSV.md](EXPORTACION_CSV.md)** - Guía de exportación de ventas
- **[RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md)** - Deploy completo en Railway
- **[VARIABLES_RAILWAY.txt](VARIABLES_RAILWAY.txt)** - Variables de entorno

---

## 🆘 Soporte

- Railway Logs: `railway logs`
- Ver deployment en Railway Dashboard
- Revisar RAILWAY_DEPLOY.md para troubleshooting
