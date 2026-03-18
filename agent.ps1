# ag_ai - OpenCode Agent Launcher (PowerShell)
param([string]$ProjectPath = "")

$agents = @{
    1  = @{ name="orchestrator";         group="PLANNING";      desc="route any complex task" }
    2  = @{ name="spec-workflow";        group="PLANNING";      desc="spec-first planning" }
    3  = @{ name="architect";            group="PLANNING";      desc="system design" }
    4  = @{ name="coder";               group="CODING";        desc="write and refactor code" }
    5  = @{ name="tdd-guide";           group="CODING";        desc="test-first development" }
    6  = @{ name="refactor-cleaner";    group="CODING";        desc="refactor without breaking" }
    7  = @{ name="build-error-resolver";group="CODING";        desc="fix build errors" }
    8  = @{ name="code-reviewer";       group="REVIEW";        desc="review code quality" }
    9  = @{ name="security-reviewer";   group="REVIEW";        desc="OWASP security audit" }
    10 = @{ name="database-reviewer";   group="REVIEW";        desc="DB schema and queries" }
    11 = @{ name="db-agent";            group="DATABASE";      desc="database specialist" }
    12 = @{ name="sql-helper";          group="DATABASE";      desc="generate SQL queries" }
    13 = @{ name="api-agent";           group="INTEGRATIONS";  desc="API design and integration" }
    14 = @{ name="telegram-bot";        group="INTEGRATIONS";  desc="Telegram bot specialist" }
    15 = @{ name="n8n-workflow";        group="INTEGRATIONS";  desc="n8n automation" }
    16 = @{ name="debugger";            group="SUPPORT";       desc="investigate bugs" }
    17 = @{ name="test-writer";         group="SUPPORT";       desc="write tests" }
    18 = @{ name="doc-updater";         group="SUPPORT";       desc="update documentation" }
}

Write-Host ""
Write-Host " ================================"
Write-Host "  OpenCode - Agent Launcher"
Write-Host " ================================"
Write-Host ""

$currentGroup = ""
foreach ($key in ($agents.Keys | Sort-Object)) {
    $a = $agents[$key]
    if ($a.group -ne $currentGroup) {
        Write-Host ""
        Write-Host " --- $($a.group) ---"
        $currentGroup = $a.group
    }
    Write-Host (" {0,2})  {1,-28} {2}" -f $key, $a.name, $a.desc)
}

Write-Host ""
Write-Host "  0)  no agent (default Build mode)"
Write-Host ""
$choice = Read-Host "  Choose (0-18)"

if ($choice -eq "0" -or $choice -eq "") {
    Write-Host ""
    Write-Host "  Starting OpenCode in default Build mode..."
    Write-Host ""
    if ($ProjectPath) { opencode $ProjectPath } else { opencode }
}
elseif ($agents.ContainsKey([int]$choice)) {
    $agent = $agents[[int]$choice].name
    $task = Read-Host "  What do you want to do?"
    $prompt = "use $agent agent to $task"
    Write-Host ""
    Write-Host "  Starting: $prompt"
    Write-Host ""
    if ($ProjectPath) { opencode run $prompt $ProjectPath } else { opencode run $prompt }
}
else {
    Write-Host "  Invalid choice."
}
