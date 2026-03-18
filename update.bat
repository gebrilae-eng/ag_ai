@echo off
setlocal

set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

echo.
echo  ag_ai - Update
echo  ==============
echo  Location: %AG_AI_DIR%
echo.

cd /d "%AG_AI_DIR%"

echo [1/2] Pulling latest from GitHub...
git fetch origin
git reset --hard origin/main
git checkout HEAD -- .
echo.

echo [2/2] Done! ag_ai is now up to date.
echo.
echo  Latest changes:
type "%AG_AI_DIR%\CHANGELOG.md" | more /P /E +1
echo.
pause
endlocal
