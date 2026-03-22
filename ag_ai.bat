@echo off
:: ── ag_ai Launcher ──────────────────────────────────────────
:: Double-click this file to open ag_ai menu in a persistent window
:: Or run: ag_ai.bat <command> [project-path]
:: ────────────────────────────────────────────────────────────
set "AG_AI_DIR=%~dp0"
if "%AG_AI_DIR:~-1%"=="\" set "AG_AI_DIR=%AG_AI_DIR:~0,-1%"

cmd /k ""%AG_AI_DIR%\run.bat""
