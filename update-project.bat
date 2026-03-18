@echo off
setlocal enabledelayedexpansion

set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

echo.
echo  ag_ai - Update Project Agents
echo  ================================
echo  Updates: agents, sub-agents, rules, templates
echo  Preserves: PROJECT.md, STACK.md, RULES.md, constitution.md
echo.

if "%~1"=="" (
    set /p PROJECT_PATH=  Project path: 
) else (
    set "PROJECT_PATH=%~1"
)

if "!PROJECT_PATH!"=="" (
    echo  Error: no project path given.
    pause
    goto :eof
)

echo  Updating agents in: !PROJECT_PATH!
echo.
python "%AG_AI_DIR%\setup_ai.py" "!PROJECT_PATH!" --update-agents

echo.
echo  Validating...
python "%AG_AI_DIR%\validate.py" "!PROJECT_PATH!"

pause
endlocal
