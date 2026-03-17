@echo off
setlocal enabledelayedexpansion

echo.
echo  ================================
echo   OpenCode - Agent Launcher
echo  ================================
echo.
echo  Pick an agent to start with:
echo.
echo  --- PLANNING ---
echo  1)  orchestrator      route any complex task
echo  2)  spec-workflow     spec-first planning
echo  3)  architect         system design
echo.
echo  --- CODING ---
echo  4)  coder             write and refactor code
echo  5)  tdd-guide         test-first development
echo  6)  refactor-cleaner  refactor without changing behavior
echo  7)  build-error-resolver  fix build errors
echo.
echo  --- REVIEW ---
echo  8)  code-reviewer     review code quality
echo  9)  security-reviewer OWASP security audit
echo  10) database-reviewer DB schema and queries
echo.
echo  --- DATABASE ---
echo  11) db-agent          database specialist
echo  12) sql-helper        generate SQL queries
echo.
echo  --- INTEGRATIONS ---
echo  13) api-agent         API design and integration
echo  14) telegram-bot      Telegram bot specialist
echo  15) n8n-workflow      n8n automation
echo.
echo  --- SUPPORT ---
echo  16) debugger          investigate bugs
echo  17) test-writer       write tests
echo  18) doc-updater       update documentation
echo.
echo  0)  no agent (default Build mode)
echo.
set /p CHOICE=  Choose (0-18): 

if "!CHOICE!"=="1"  set AGENT=orchestrator
if "!CHOICE!"=="2"  set AGENT=spec-workflow
if "!CHOICE!"=="3"  set AGENT=architect
if "!CHOICE!"=="4"  set AGENT=coder
if "!CHOICE!"=="5"  set AGENT=tdd-guide
if "!CHOICE!"=="6"  set AGENT=refactor-cleaner
if "!CHOICE!"=="7"  set AGENT=build-error-resolver
if "!CHOICE!"=="8"  set AGENT=code-reviewer
if "!CHOICE!"=="9"  set AGENT=security-reviewer
if "!CHOICE!"=="10" set AGENT=database-reviewer
if "!CHOICE!"=="11" set AGENT=db-agent
if "!CHOICE!"=="12" set AGENT=sql-helper
if "!CHOICE!"=="13" set AGENT=api-agent
if "!CHOICE!"=="14" set AGENT=telegram-bot
if "!CHOICE!"=="15" set AGENT=n8n-workflow
if "!CHOICE!"=="16" set AGENT=debugger
if "!CHOICE!"=="17" set AGENT=test-writer
if "!CHOICE!"=="18" set AGENT=doc-updater
if "!CHOICE!"=="0"  set AGENT=

if "!AGENT!"=="" (
    echo.
    echo  Starting OpenCode in default Build mode...
    echo.
    opencode %1
) else (
    echo.
    echo  Starting OpenCode with agent: !AGENT!
    echo.
    opencode --agent !AGENT! %1
)

endlocal
