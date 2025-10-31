@echo off
echo ========================================
echo   Fix: Demasiados redirects
echo   Desplegando correccion...
echo ========================================
echo.

echo [1/3] Agregando cambios...
git add .

echo.
echo [2/3] Commit...
git commit -m "Fix: Eliminar SECURE_SSL_REDIRECT para Railway"

echo.
echo [3/3] Push a Railway...
git push origin main

echo.
echo ========================================
echo   Deploy iniciado!
echo   Espera 2 minutos y prueba de nuevo
echo ========================================
echo.
pause
