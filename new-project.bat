@echo off
setlocal enabledelayedexpansion

set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

echo.
echo  ================================
echo   ag_ai - New Project Setup
echo  ================================
echo.

set /p PROJECT_NAME=  Project name: 
if "!PROJECT_NAME!"=="" set PROJECT_NAME=my-project

echo.
echo  Where to create the project?
echo  1) C:\laragon\www\
echo  2) D:\projects\
echo  3) F:\
echo  4) Custom path
echo.
set /p LOCATION_CHOICE=  Choose (1-4): 

if "!LOCATION_CHOICE!"=="1" set BASE_PATH=C:\laragon\www
if "!LOCATION_CHOICE!"=="2" set BASE_PATH=D:\projects
if "!LOCATION_CHOICE!"=="3" set BASE_PATH=F:
if "!LOCATION_CHOICE!"=="4" (
    set /p BASE_PATH=  Enter path: 
)
if "!BASE_PATH!"=="" set BASE_PATH=C:\laragon\www

set "PROJECT_PATH=!BASE_PATH!\!PROJECT_NAME!"

if exist "!PROJECT_PATH!\CLAUDE.md" (
    echo.
    echo  ============================================================
    echo   WARNING: !PROJECT_PATH! already has an ag_ai project!
    echo  ============================================================
    set /p CONFIRM=  Overwrite existing project? [y/N]: 
    if /i not "!CONFIRM!"=="y" (
        echo  Cancelled.
        pause
        goto :eof
    )
    echo.
)

echo.
echo  Creating: !PROJECT_PATH!
echo.

mkdir "!PROJECT_PATH!" 2>nul

echo  [1/3] Installing AI infrastructure...
python "%AG_AI_DIR%\setup_ai.py" "!PROJECT_PATH!" --auto

echo  [2/3] Setting up project context...
python "%AG_AI_DIR%\wizard.py" "!PROJECT_PATH!"

echo  [3/3] Validating setup...
python "%AG_AI_DIR%\validate.py" "!PROJECT_PATH!"

echo.
echo  Done! Project ready at: !PROJECT_PATH!
echo.
echo  Next:
echo    cd "!PROJECT_PATH!"
echo    claude    or    opencode
echo.
pause
endlocal
