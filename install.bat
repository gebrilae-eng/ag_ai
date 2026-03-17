@echo off
echo.
echo  ag_ai - Update and Install
echo  ===========================
echo.

cd /d C:\temp\ag_ai

echo [1/3] Pulling latest from GitHub...
git fetch origin
git reset --hard origin/main
echo.

echo [2/3] Running setup...
if "%1"=="" (
    python setup_ai.py
) else (
    python setup_ai.py %1
)
echo.
echo [3/3] Done!
pause
