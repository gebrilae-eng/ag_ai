@echo off
setlocal enabledelayedexpansion

set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

if "%~1"=="" goto :menu

:: Direct call: run.bat install / wizard / validate / update / update-project / new-project / agent
set "CMD=%~1"
shift
if /i "!CMD!"=="install"        ( python "%AG_AI_DIR%\setup_ai.py" %* & goto :eof )
if /i "!CMD!"=="wizard"         ( python "%AG_AI_DIR%\wizard.py"   %* & goto :eof )
if /i "!CMD!"=="validate"       ( python "%AG_AI_DIR%\validate.py" %* & goto :eof )
if /i "!CMD!"=="update"         ( call "%AG_AI_DIR%\scripts\update.bat"         & goto :eof )
if /i "!CMD!"=="update-project" ( python "%AG_AI_DIR%\setup_ai.py" %* --update-agents & goto :eof )
if /i "!CMD!"=="new-project"    ( call "%AG_AI_DIR%\scripts\new-project.bat"    & goto :eof )
if /i "!CMD!"=="agent"          ( call "%AG_AI_DIR%\agent.bat"     %* & goto :eof )
echo  Unknown command: !CMD!
goto :eof

:menu
echo.
echo  ================================
echo   ag_ai v2.5
echo  ================================
echo.
echo  --- SETUP ---
echo   1) new-project    create + install + wizard
echo   2) install        install agents into a project
echo   3) wizard         fill context files
echo   4) validate       check project setup
echo.
echo  --- UPDATE ---
echo   5) update         update ag_ai from GitHub
echo   6) update-project update agents in a project (keep context)
echo.
echo  --- WORK ---
echo   7) agent          launch OpenCode with agent menu
echo.
set /p CHOICE=  Choose (1-7): 

if "!CHOICE!"=="1" ( python "%AG_AI_DIR%\setup_ai.py" --auto & python "%AG_AI_DIR%\wizard.py" & goto :eof )
if "!CHOICE!"=="2" ( python "%AG_AI_DIR%\setup_ai.py" & goto :eof )
if "!CHOICE!"=="3" ( python "%AG_AI_DIR%\wizard.py"   & goto :eof )
if "!CHOICE!"=="4" ( python "%AG_AI_DIR%\validate.py" & pause & goto :eof )
if "!CHOICE!"=="5" ( cd /d "%AG_AI_DIR%" & git fetch origin & git reset --hard origin/main & echo Done. & pause & goto :eof )
if "!CHOICE!"=="6" ( set /p PROJ=  Project path: & python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --update-agents & pause & goto :eof )
if "!CHOICE!"=="7" ( call "%AG_AI_DIR%\agent.bat" & goto :eof )

echo  Invalid choice.
pause
endlocal
