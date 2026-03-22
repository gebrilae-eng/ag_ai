@echo off
chcp 65001 >nul
title ag_ai v3.0

setlocal EnableDelayedExpansion

set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

if not exist "%AG_AI_DIR%\setup_ai.py" (
    echo.
    echo  ERROR: setup_ai.py not found in: %AG_AI_DIR%
    echo  Run from: C:\ag_ai\run.bat
    echo.
    pause
    exit /b 1
)

if not "%~1"=="" (
    set "CMD=%~1"
    set "ARG2=%~2"
    if /i "!CMD!"=="install"        ( python "%AG_AI_DIR%\setup_ai.py" "!ARG2!" & pause & exit /b )
    if /i "!CMD!"=="wizard"         ( python "%AG_AI_DIR%\wizard.py"   "!ARG2!" & pause & exit /b )
    if /i "!CMD!"=="validate"       ( python "%AG_AI_DIR%\validate.py" "!ARG2!" & pause & exit /b )
    if /i "!CMD!"=="prd"            ( python "%AG_AI_DIR%\prd.py"      "!ARG2!" --regenerate & pause & exit /b )
    if /i "!CMD!"=="update"         ( call :do_update_ag_ai & exit /b )
    if /i "!CMD!"=="update-agency"  ( call :do_update_agency & exit /b )
    if /i "!CMD!"=="update-project" ( python "%AG_AI_DIR%\setup_ai.py" "!ARG2!" --update-agents & pause & exit /b )
    if /i "!CMD!"=="agent"          ( call "%AG_AI_DIR%\agent.bat" & exit /b )
    echo  Unknown command: !CMD!
    pause & exit /b 1
)


:menu
cls
echo.
echo  ag_ai x agency-agents v3.0
echo  ================================================
echo   1) new-project    create + install + wizard + PRD
echo   2) install        ag_ai + agency-agents into project
echo   3) install-agency agency-agents divisions only
echo   4) wizard         fill context files
echo   5) validate       check project setup
echo   6) prd            generate/update PRD.md
echo   7) update         update ag_ai from GitHub
echo   8) update-agency  update agency-agents cache
echo   9) update-project update agents (keep context)
echo  10) agent          launch OpenCode agent menu
echo  11) agency         browse divisions list
echo   0) exit
echo.
set /p "CHOICE=  Choose: "
echo.

if "!CHOICE!"=="0"  exit /b 0
if "!CHOICE!"=="1"  call :do_new           & goto :menu
if "!CHOICE!"=="2"  call :do_install       & goto :menu
if "!CHOICE!"=="3"  call :do_install_agency & goto :menu
if "!CHOICE!"=="4"  call :do_wizard        & goto :menu
if "!CHOICE!"=="5"  call :do_validate      & goto :menu
if "!CHOICE!"=="6"  call :do_prd           & goto :menu
if "!CHOICE!"=="7"  call :do_update_ag_ai  & goto :menu
if "!CHOICE!"=="8"  call :do_update_agency & goto :menu
if "!CHOICE!"=="9"  call :do_update_project & goto :menu
if "!CHOICE!"=="10" ( call "%AG_AI_DIR%\agent.bat" & goto :menu )
if "!CHOICE!"=="11" call :do_agency_info   & goto :menu
echo  Invalid. Try again.
pause
goto :menu


:do_new
    set "PROJ="
    set /p "PROJ=  Project path [D:\my-project]: "
    if "!PROJ!"=="" set "PROJ=D:\my-project"
    echo.
    echo  [1/3] Installing...
    python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --auto
    echo  [2/3] Wizard...
    python "%AG_AI_DIR%\wizard.py" "!PROJ!"
    echo  [3/3] PRD...
    python "%AG_AI_DIR%\prd.py" "!PROJ!" --regenerate
    echo.
    echo  Done: !PROJ!
    pause
    exit /b 0

:do_install
    set "PROJ="
    set /p "PROJ=  Project path: "
    echo.
    echo  1) Dev essentials   2) All 15 divisions   3) Custom   4) ag_ai only
    set "DIVS="
    set /p "DIVS=  Choose [1]: "
    if "!DIVS!"=="2" ( python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --all-divisions )
    if "!DIVS!"=="3" (
        set "CUSTOM="
        echo  Options: engineering design marketing product project-management
        echo           testing support specialized game-development academic
        set /p "CUSTOM=  Divisions (comma-separated): "
        python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --divisions "!CUSTOM!"
    )
    if "!DIVS!"=="4" ( python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --ag-only )
    if "!DIVS!"==""  ( python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" )
    if "!DIVS!"=="1" ( python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" )
    pause
    exit /b 0

:do_install_agency
    set "PROJ="
    set /p "PROJ=  Project path: "
    echo.
    echo  1) Dev essentials [default]   2) All 15 divisions
    set "DIVS="
    set /p "DIVS=  Choose [1]: "
    if "!DIVS!"=="2" ( python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --all-divisions ) else ( python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" )
    pause
    exit /b 0

:do_wizard
    set "PROJ="
    set /p "PROJ=  Project path: "
    python "%AG_AI_DIR%\wizard.py" "!PROJ!"
    pause
    exit /b 0

:do_validate
    set "PROJ="
    set /p "PROJ=  Project path: "
    python "%AG_AI_DIR%\validate.py" "!PROJ!"
    pause
    exit /b 0

:do_prd
    set "PROJ="
    set /p "PROJ=  Project path: "
    python "%AG_AI_DIR%\prd.py" "!PROJ!" --regenerate
    pause
    exit /b 0

:do_update_project
    set "PROJ="
    set /p "PROJ=  Project path: "
    python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --update-agents
    pause
    exit /b 0

:do_update_ag_ai
    echo  Updating ag_ai from GitHub (cache preserved)...
    cd /d "%AG_AI_DIR%"
    git fetch origin
    git pull --ff-only origin main
    if !ERRORLEVEL! NEQ 0 ( git pull --rebase origin main )
    echo  Done.
    pause
    exit /b 0

:do_update_agency
    echo  Updating agency-agents cache...
    if exist "%AG_AI_DIR%\.agency-agents-cache\.git" (
        git -C "%AG_AI_DIR%\.agency-agents-cache" pull --ff-only
        echo  Done.
    ) else (
        echo  No cache - will clone on next install.
    )
    pause
    exit /b 0

:do_agency_info
    echo.
    echo  Division              Agents
    echo  ----------------------------------
    echo  engineering             23
    echo  marketing               27
    echo  specialized             27
    echo  design                   8
    echo  sales                    8
    echo  testing                  8
    echo  paid-media               7
    echo  support                  6
    echo  spatial-computing        6
    echo  project-management       6
    echo  product                  5
    echo  game-development         5
    echo  academic                 5
    echo  strategy                 3
    echo  integrations             1
    echo.
    pause
    exit /b 0

