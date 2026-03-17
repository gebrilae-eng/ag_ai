@echo off
setlocal

echo.
echo  ag_ai - Update and Install
echo  ===========================
echo.

:: Get the directory where install.bat lives (wherever ag_ai is cloned)
set "AG_AI_DIR=%~dp0"
:: Remove trailing backslash
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

echo  ag_ai location: %AG_AI_DIR%
echo.

cd /d "%AG_AI_DIR%"

echo [1/3] Pulling latest from GitHub...
git fetch origin
git reset --hard origin/main
echo.

echo [2/3] Running setup...
if "%1"=="" (
    python "%AG_AI_DIR%\setup_ai.py"
) else (
    python "%AG_AI_DIR%\setup_ai.py" %1
)
echo.
echo [3/3] Done!
pause

endlocal
