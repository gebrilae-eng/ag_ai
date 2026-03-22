@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

:: ── Direct mode: run.bat <command> <project-path> ────────────────────────────
if not "%~1"=="" (
    set "CMD=%~1"
    set "ARG2=%~2"
    if /i "!CMD!"=="install"        ( python "%AG_AI_DIR%\setup_ai.py" "!ARG2!" & goto :eof )
    if /i "!CMD!"=="wizard"         ( python "%AG_AI_DIR%\wizard.py"   "!ARG2!" & goto :eof )
    if /i "!CMD!"=="validate"       ( python "%AG_AI_DIR%\validate.py" "!ARG2!" & goto :eof )
    if /i "!CMD!"=="prd"            ( python "%AG_AI_DIR%\prd.py"      "!ARG2!" --regenerate & goto :eof )
    if /i "!CMD!"=="update"         goto :do_update_ag_ai
    if /i "!CMD!"=="update-agency"  goto :do_update_agency
    if /i "!CMD!"=="update-project" ( python "%AG_AI_DIR%\setup_ai.py" "!ARG2!" --update-agents & goto :eof )
    if /i "!CMD!"=="new-project"    ( set "PROJ=!ARG2!" & goto :do_new )
    if /i "!CMD!"=="agent"          ( call "%AG_AI_DIR%\agent.bat" & goto :eof )
    if /i "!CMD!"=="agency"         goto :agency_info
    echo  Unknown command: !CMD!
    goto :eof
)


:: ── Interactive menu ─────────────────────────────────────────────────────────
:menu
cls
echo.
echo  ag_ai x agency-agents v3.0
echo  AI Dev Infrastructure + 192 Specialist Agents
echo  ================================================
echo.
echo   SETUP
echo   1)  new-project     create + install + wizard + PRD
echo   2)  install         install ag_ai + agency-agents
echo   3)  install-agency  install agency-agents divisions only
echo   4)  wizard          fill context files
echo   5)  validate        check project setup
echo   6)  prd             generate/update PRD.md
echo.
echo   UPDATE
echo   7)  update          update ag_ai from GitHub
echo   8)  update-agency   update agency-agents cache
echo   9)  update-project  update agents in project (keep context)
echo.
echo   WORK
echo   10) agent           launch OpenCode with agent menu
echo   11) agency          browse agency-agents divisions
echo.
set /p "CHOICE=  Choose (1-11): "

if "!CHOICE!"=="1"  goto :do_new
if "!CHOICE!"=="2"  goto :do_install
if "!CHOICE!"=="3"  goto :do_install_agency
if "!CHOICE!"=="4"  ( python "%AG_AI_DIR%\wizard.py"   & pause & goto :eof )
if "!CHOICE!"=="5"  ( python "%AG_AI_DIR%\validate.py" & pause & goto :eof )
if "!CHOICE!"=="6"  goto :do_prd
if "!CHOICE!"=="7"  goto :do_update_ag_ai
if "!CHOICE!"=="8"  goto :do_update_agency
if "!CHOICE!"=="9"  goto :do_update_project
if "!CHOICE!"=="10" ( call "%AG_AI_DIR%\agent.bat" & goto :eof )
if "!CHOICE!"=="11" goto :agency_info
echo  Invalid choice.
pause & goto :menu


:do_new
    if "!PROJ!"=="" set /p "PROJ=  Project path [D:\my-project]: "
    if "!PROJ!"=="" set "PROJ=D:\my-project"
    echo.
    echo  [1/3] Installing ag_ai + agency-agents...
    python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --auto
    echo  [2/3] Running wizard...
    python "%AG_AI_DIR%\wizard.py" "!PROJ!"
    echo  [3/3] Generating PRD...
    python "%AG_AI_DIR%\prd.py" "!PROJ!" --regenerate
    echo.
    echo  Done! Project ready at: !PROJ!
    pause & goto :eof

:do_install
    set /p "PROJ=  Project path: "
    echo.
    echo  Divisions: 1) Dev essentials  2) All 15  3) Custom  4) ag_ai only
    set /p "DIVS=  Choose [1-4, default 1]: "
    if "!DIVS!"=="2" ( python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --all-divisions & pause & goto :eof )
    if "!DIVS!"=="3" (
        echo  Available: engineering design marketing sales product project-management
        echo             testing support spatial-computing specialized game-development academic
        set /p "CUSTOM=  Divisions (comma-separated): "
        python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --divisions "!CUSTOM!" & pause & goto :eof
    )
    if "!DIVS!"=="4" ( python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --ag-only & pause & goto :eof )
    python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" & pause & goto :eof

:do_install_agency
    set /p "PROJ=  Project path: "
    echo.
    echo  1) Dev essentials (default)   2) All 15 divisions
    set /p "DIVS=  Choose [1-2]: "
    if "!DIVS!"=="2" ( python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --all-divisions & pause & goto :eof )
    python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" & pause & goto :eof

:do_prd
    set /p "PROJ=  Project path: "
    python "%AG_AI_DIR%\prd.py" "!PROJ!" --regenerate & pause & goto :eof

:do_update_project
    set /p "PROJ=  Project path: "
    python "%AG_AI_DIR%\setup_ai.py" "!PROJ!" --update-agents & pause & goto :eof


:do_update_ag_ai
    echo.
    echo  Updating ag_ai from GitHub...
    echo  (Keeps .agency-agents-cache intact)
    cd /d "%AG_AI_DIR%"
    git fetch origin
    git pull --ff-only origin main
    if !ERRORLEVEL! NEQ 0 (
        echo  Trying rebase...
        git pull --rebase origin main
    )
    echo.
    echo  ag_ai updated successfully.
    pause & goto :eof

:do_update_agency
    echo.
    echo  Updating agency-agents cache...
    if exist "%AG_AI_DIR%\.agency-agents-cache\.git" (
        git -C "%AG_AI_DIR%\.agency-agents-cache" pull --ff-only
        echo  Cache updated. Re-run install to push to projects.
    ) else (
        echo  No cache found. Cache will be created on next install.
    )
    pause & goto :eof

:agency_info
    cls
    echo.
    echo  agency-agents -- 192 Agents / 15 Divisions
    echo  ============================================
    echo.
    echo   Division              Agents  Best for
    echo   --------------------------------------------------
    echo   engineering             23    Backend, Frontend, DevOps, Security
    echo   marketing               27    SEO, Content, Growth, Social
    echo   specialized             27    MCP, Blockchain, AI/ML, Data
    echo   design                   8    UI, UX, Brand
    echo   sales                    8    Discovery, Deal Strategy
    echo   testing                  8    QA, Reality Check, API Testing
    echo   paid-media               7    Ads, Analytics
    echo   support                  6    Customer, Analytics
    echo   spatial-computing        6    XR, visionOS, AR
    echo   project-management       6    Agile, Scrum, Studio
    echo   product                  5    Product Manager, Research
    echo   game-development         5    Unity, Unreal, Narrative
    echo   academic                 5    Research, World-building
    echo   strategy                 3    Business Strategy
    echo   integrations             1    Platform Integration
    echo.
    echo   Usage in OpenCode:
    echo   use engineering-backend-engineer agent to build [feature]
    echo   use testing-reality-checker agent to verify [module]
    echo   use product-product-manager agent to write PRD for [feature]
    echo.
    pause & goto :eof

endlocal
