# 🚀 Despliegue en Railway - MI_tienda

## 📋 Variables de Entorno para Railway

Copia y pega estas variables en el panel de Railway:

### **Variables de Base de Datos (Supabase)**
```
user=postgres.eqvpkknjgfzeoxibqype
password=Vicho.01112005
host=aws-1-us-east-2.pooler.supabase.com
port=6543
dbname=postgres
```

### **Variables de Django**
```
SECRET_KEY=prod-mi-tienda-2025-x9k2m4n5p6q7r8s9t0-secure-key-railway
DEBUG=False
ALLOWED_HOSTS=mitienda-production.up.railway.app,localhost,127.0.0.1
PORT=8000
RAILWAY_ENVIRONMENT=production
```

### **Variables opcionales** (Railway las configura automáticamente)
```
PYTHONUNBUFFERED=1
```

---

## 🔧 Configuración en Railway (Paso a Paso)

### **1. Configurar Variables de Entorno**

Ve a tu proyecto en Railway → **Variables** y agrega:

| Variable | Valor |
|----------|-------|
| `user` | `postgres.eqvpkknjgfzeoxibqype` |
| `password` | `Vicho.01112005` |
| `host` | `aws-1-us-east-2.pooler.supabase.com` |
| `port` | `6543` |
| `dbname` | `postgres` |
| `SECRET_KEY` | `prod-mi-tienda-2025-x9k2m4n5p6q7r8s9t0-secure-key-railway` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `mitienda-production.up.railway.app,localhost,127.0.0.1` |
| `PORT` | `8000` |
| `RAILWAY_ENVIRONMENT` | `production` |
| `PYTHONUNBUFFERED` | `1` |

### **2. Configurar Networking**

1. Ve a **Settings** → **Networking**
2. Verifica que el puerto esté en **8000**
3. Copia tu dominio: `mitienda-production.up.railway.app`

### **3. Configurar Build & Deploy**

En **Settings** → **Deploy**:
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `cd tienda && python manage.py collectstatic --noinput && python manage.py migrate && gunicorn tienda.wsgi:application --bind 0.0.0.0:$PORT`

---

## 📦 Archivos Necesarios (Ya Creados)

✅ `requirements.txt` - Dependencias Python  
✅ `Procfile` - Comando de inicio  
✅ `railway.json` - Configuración Railway  
✅ `runtime.txt` - Versión de Python (3.12)  
✅ `.gitignore` - Archivos ignorados  

---

## 🚢 Desplegar en Railway

### **Opción 1: Desde GitHub (Recomendado)**

1. **Push al repositorio:**
```bash
git add .
git commit -m "Configuración para Railway"
git push origin main
```

2. **Railway detectará los cambios automáticamente** y comenzará el deploy

3. **Espera el deploy** (2-3 minutos)

4. **Accede a tu app:** `https://mitienda-production.up.railway.app`

### **Opción 2: Desde CLI de Railway**

```bash
# Instalar Railway CLI
npm i -g @railway/cli

# Login
railway login

# Link al proyecto
railway link

# Deploy
railway up
```

---

## ✅ Verificar el Deploy

### **1. Ver logs en Railway**
Ve a **Deployments** → Click en el último deploy → **View Logs**

### **2. Probar la aplicación**
```
https://mitienda-production.up.railway.app
https://mitienda-production.up.railway.app/admin
```

### **3. Crear superusuario (si es necesario)**

Desde la terminal de Railway o ejecuta:
```bash
railway run python tienda/manage.py createsuperuser
```

---

## 🐛 Solución de Problemas

### **Error: "DisallowedHost"**
✅ Verifica que `ALLOWED_HOSTS` incluya tu dominio de Railway

### **Error: "Static files not found"**
✅ Ejecuta: `railway run python tienda/manage.py collectstatic`

### **Error de base de datos**
✅ Verifica las variables de Supabase
✅ Ejecuta: `railway run python tienda/manage.py migrate`

### **Ver logs en tiempo real**
```bash
railway logs
```

---

## 🔐 Seguridad en Producción

✅ **DEBUG=False** - Deshabilita modo debug  
✅ **SECRET_KEY** - Usa una clave única y segura  
✅ **SSL/HTTPS** - Railway lo provee automáticamente  
✅ **CSRF_TRUSTED_ORIGINS** - Ya configurado  
✅ **Secure Cookies** - Activados automáticamente en producción  

---

## 📊 Después del Deploy

### **Crear superusuario:**
```bash
railway run python tienda/manage.py createsuperuser
```

### **Acceder al admin:**
```
https://mitienda-production.up.railway.app/admin/
```

### **Ver estadísticas:**
Ve a Railway → **Metrics** para ver:
- CPU usage
- Memory usage
- Network traffic
- Request logs

---

## 🔄 Actualizar la Aplicación

Cada vez que hagas cambios:

```bash
git add .
git commit -m "Descripción de cambios"
git push origin main
```

Railway automáticamente:
1. Detecta los cambios
2. Instala dependencias
3. Ejecuta migraciones
4. Reinicia la aplicación

---

## 📝 Notas Importantes

1. **No subas el .env al repositorio** (ya está en .gitignore)
2. **Todas las variables deben estar en Railway**
3. **Railway ejecuta automáticamente las migraciones**
4. **Los logs se guardan por 7 días**
5. **El dominio es permanente** (puedes agregar uno custom)

---

## ✅ Checklist Final

- [ ] Variables de entorno configuradas en Railway
- [ ] Puerto 8000 configurado en Networking
- [ ] Dominio correcto en ALLOWED_HOSTS
- [ ] Push al repositorio de GitHub
- [ ] Deploy exitoso (check logs)
- [ ] Aplicación accesible en el dominio
- [ ] Admin panel funcionando
- [ ] Base de datos Supabase conectada
- [ ] Archivos estáticos cargando correctamente

---

## 🎉 ¡Listo!

Tu aplicación está en producción en:
**https://mitienda-production.up.railway.app**

Para soporte o dudas:
- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
