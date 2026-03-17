@echo off
setlocal

set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

echo.
echo  ag_ai - Project Setup Wizard
echo  ==============================
echo.

if "%~1"=="" (
    python "%AG_AI_DIR%\wizard.py"
) else (
    python "%AG_AI_DIR%\wizard.py" "%~1"
)

pause
endlocal
