@echo off
echo ========================================
echo   Solucionando error de migraciones
echo ========================================
echo.

cd tienda

echo [1/3] Creando migraciones...
python manage.py makemigrations

echo.
echo [2/3] Aplicando migraciones localmente...
python manage.py migrate

echo.
echo [3/3] Ahora haz el deploy...
echo.
echo ========================================
echo   Migraciones creadas!
echo   Ahora ejecuta: deploy.bat
echo ========================================
echo.
pause
