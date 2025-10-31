@echo off
echo ========================================
echo   Desplegando a Railway
echo ========================================
echo.

echo [1/4] Agregando archivos al repositorio...
git add .

echo.
echo [2/4] Creando commit...
set /p mensaje="Mensaje del commit: "
git commit -m "%mensaje%"

echo.
echo [3/4] Subiendo a GitHub...
git push origin main

echo.
echo [4/4] Railway detectara los cambios automaticamente
echo.
echo ========================================
echo   Deploy iniciado!
echo   Revisa los logs en Railway
echo ========================================
echo.
pause
