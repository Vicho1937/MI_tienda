@echo off
echo Iniciando servidor con Supabase...
echo.
cd tienda
python manage.py migrate
python manage.py runserver
pause
