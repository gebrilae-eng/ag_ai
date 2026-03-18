@echo off
setlocal enabledelayedexpansion

set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

echo.
echo  ================================
echo   ag_ai v2.3
echo  ================================
echo.
echo  What do you want to do?
echo.
echo  --- SETUP ---
echo   1) new-project    create + install + wizard
echo   2) install        install agents into a project
echo   3) wizard         fill context files (PROJECT/STACK/RULES)
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

if "!CHOICE!"=="1" call "%AG_AI_DIR%\new-project.bat"    & goto :eof
if "!CHOICE!"=="2" call "%AG_AI_DIR%\install.bat" %*     & goto :eof
if "!CHOICE!"=="3" call "%AG_AI_DIR%\wizard.bat" %*      & goto :eof
if "!CHOICE!"=="4" call "%AG_AI_DIR%\validate.bat" %*    & goto :eof
if "!CHOICE!"=="5" call "%AG_AI_DIR%\update.bat"         & goto :eof
if "!CHOICE!"=="6" call "%AG_AI_DIR%\update-project.bat" %* & goto :eof
if "!CHOICE!"=="7" call "%AG_AI_DIR%\agent.bat" %*       & goto :eof

echo  Invalid choice.
pause
endlocal
