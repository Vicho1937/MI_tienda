# 🚀 DEPLOY RAILWAY - GUÍA RÁPIDA

## 📋 PASO 1: Configurar Variables en Railway

Ir a tu proyecto en Railway → **Variables** → Agregar estas 11 variables:

```
user=postgres.eqvpkknjgfzeoxibqype
password=Vicho.01112005
host=aws-1-us-east-2.pooler.supabase.com
port=6543
dbname=postgres
SECRET_KEY=prod-mi-tienda-2025-x9k2m4n5p6q7r8s9t0-secure-key-railway
DEBUG=False
ALLOWED_HOSTS=mitienda-production.up.railway.app,localhost,127.0.0.1
PORT=8000
RAILWAY_ENVIRONMENT=production
PYTHONUNBUFFERED=1
```

## 🚢 PASO 2: Hacer Deploy

Ejecuta desde la raíz del proyecto:

```bash
deploy.bat
```

O manualmente:
```bash
git add .
git commit -m "Deploy a Railway"
git push origin main
```

## ⏳ PASO 3: Esperar (2-3 minutos)

Railway automáticamente:
1. ✅ Detecta los cambios
2. ✅ Instala dependencias (`requirements.txt`)
3. ✅ Ejecuta migraciones (`python manage.py migrate`)
4. ✅ Recolecta archivos estáticos (`collectstatic`)
5. ✅ Inicia la aplicación con Gunicorn

## ✅ PASO 4: Verificar

Abre en tu navegador:
- **App:** https://mitienda-production.up.railway.app
- **Admin:** https://mitienda-production.up.railway.app/admin

## 👤 PASO 5: Crear Superusuario (Opcional)

Desde Railway CLI:
```bash
railway login
railway link
railway run python tienda/manage.py createsuperuser
```

O desde la consola web de Railway.

## 🎉 ¡LISTO!

Tu aplicación está en producción conectada a Supabase.

---

## 📚 Documentación Completa

- **RAILWAY_DEPLOY.md** - Guía detallada completa
- **CHECKLIST_DEPLOY.md** - Checklist paso a paso
- **VARIABLES_RAILWAY.txt** - Solo las variables
- **EXPORTACION_CSV.md** - Guía de exportación

---

## 🆘 Problemas Comunes

### Error 503 / App no carga
```bash
# Revisar logs
railway logs

# Verificar puerto
PORT=8000 en variables

# Verificar ALLOWED_HOSTS
Debe incluir: mitienda-production.up.railway.app
```

### Error de Base de Datos
```bash
# Ejecutar migraciones manualmente
railway run python tienda/manage.py migrate

# Verificar variables de Supabase
host, user, password, dbname, port
```

### Static files 404
```bash
# Recolectar archivos estáticos
railway run python tienda/manage.py collectstatic --noinput
```

---

## 📞 Soporte

- Railway Dashboard: https://railway.app/dashboard
- Logs: Click en tu proyecto → Deployments → View Logs
- Railway Discord: https://discord.gg/railway
