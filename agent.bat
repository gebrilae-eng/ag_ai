@echo off
setlocal enabledelayedexpansion

echo.
echo  ================================
echo   ag_ai - Agent Launcher
echo  ================================
echo.
echo  --- PLANNING ---
echo   1) orchestrator     route any complex task (delegates only)
echo   2) spec-workflow    spec-first planning
echo   3) architect        system design
echo.
echo  --- DEVELOPMENT ---
echo   4) coder            write and refactor code
echo   5) tdd-guide        test-first development
echo   6) db-agent         database specialist
echo   7) api-agent        API design and integration
echo   8) refactor-cleaner refactor without breaking
echo   9) build-error-resolver  fix build errors
echo.
echo  --- REVIEW ---
echo  10) code-reviewer    review code quality
echo  11) security-reviewer OWASP security audit
echo  12) database-reviewer DB schema and queries
echo  13) doc-updater      update documentation
echo.
echo  --- SPECIALISTS ---
echo  14) sql-helper       generate SQL queries
echo  15) telegram-bot     Telegram bot specialist
echo  16) n8n-workflow     n8n automation
echo  17) debugger         investigate bugs
echo  18) test-writer      write tests
echo.
echo   0) no agent (default Build mode)
echo.
set /p CHOICE=  Choose (0-18): 

if "!CHOICE!"=="1"  set AGENT=orchestrator
if "!CHOICE!"=="2"  set AGENT=spec-workflow
if "!CHOICE!"=="3"  set AGENT=architect
if "!CHOICE!"=="4"  set AGENT=coder
if "!CHOICE!"=="5"  set AGENT=tdd-guide
if "!CHOICE!"=="6"  set AGENT=db-agent
if "!CHOICE!"=="7"  set AGENT=api-agent
if "!CHOICE!"=="8"  set AGENT=refactor-cleaner
if "!CHOICE!"=="9"  set AGENT=build-error-resolver
if "!CHOICE!"=="10" set AGENT=code-reviewer
if "!CHOICE!"=="11" set AGENT=security-reviewer
if "!CHOICE!"=="12" set AGENT=database-reviewer
if "!CHOICE!"=="13" set AGENT=doc-updater
if "!CHOICE!"=="14" set AGENT=sql-helper
if "!CHOICE!"=="15" set AGENT=telegram-bot
if "!CHOICE!"=="16" set AGENT=n8n-workflow
if "!CHOICE!"=="17" set AGENT=debugger
if "!CHOICE!"=="18" set AGENT=test-writer
if "!CHOICE!"=="0"  set AGENT=

if defined AGENT (
    set /p TASK=  What do you want to do? 
    echo.
    echo  Starting: use !AGENT! agent to !TASK!
    echo.
    if "%1"=="" (
        opencode run "use !AGENT! agent to !TASK!"
    ) else (
        opencode run "use !AGENT! agent to !TASK!" %1
    )
) else (
    echo.
    echo  Starting OpenCode in default Build mode...
    echo.
    if "%1"=="" ( opencode ) else ( opencode %1 )
)

endlocal
