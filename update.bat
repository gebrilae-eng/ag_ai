@echo off
setlocal

set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

echo.
echo  ag_ai - Force Update
echo  ====================
echo  Location: %AG_AI_DIR%
echo.

cd /d "%AG_AI_DIR%"

echo Fetching latest from GitHub...
git fetch origin

echo Resetting to latest...
git reset --hard origin/main

echo.
echo Done! ag_ai is now up to date.
echo.
pause

endlocal
