@echo off
setlocal

set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

if "%~1"=="" (
    python "%AG_AI_DIR%\validate.py"
) else (
    python "%AG_AI_DIR%\validate.py" "%~1"
)

pause
endlocal
