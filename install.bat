@echo off
setlocal

echo.
echo  ag_ai - Install
echo  ================
echo.

set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

echo  ag_ai location: %AG_AI_DIR%
echo.

echo [1/2] Running setup...
if "%~1"=="" (
    python "%AG_AI_DIR%\setup_ai.py"
) else (
    python "%AG_AI_DIR%\setup_ai.py" "%~1"
)

echo.
echo [2/2] Done!
echo.
echo  Tip: to update ag_ai itself run update.bat
pause
endlocal
