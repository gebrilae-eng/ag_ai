# ag_ai - Agent Launcher (PowerShell)
param([string]$ProjectPath = "")

$agents = [ordered]@{
    # Planning
    1  = @{ name="orchestrator";         group="PLANNING";     desc="route any complex task (delegates only)" }
    2  = @{ name="spec-workflow";        group="PLANNING";     desc="spec-first planning" }
    3  = @{ name="architect";            group="PLANNING";     desc="system design" }
    # Development
    4  = @{ name="coder";               group="DEVELOPMENT";  desc="write and refactor code" }
    5  = @{ name="tdd-guide";           group="DEVELOPMENT";  desc="test-first development" }
    6  = @{ name="db-agent";            group="DEVELOPMENT";  desc="database specialist" }
    7  = @{ name="api-agent";           group="DEVELOPMENT";  desc="API design and integration" }
    8  = @{ name="refactor-cleaner";    group="DEVELOPMENT";  desc="refactor without breaking" }
    9  = @{ name="build-error-resolver";group="DEVELOPMENT";  desc="fix build errors" }
    # Review
    10 = @{ name="code-reviewer";       group="REVIEW";       desc="review code quality" }
    11 = @{ name="security-reviewer";   group="REVIEW";       desc="OWASP security audit" }
    12 = @{ name="database-reviewer";   group="REVIEW";       desc="DB schema and queries" }
    13 = @{ name="doc-updater";         group="REVIEW";       desc="update documentation" }
    # Specialists
    14 = @{ name="sql-helper";          group="SPECIALISTS";  desc="generate SQL queries" }
    15 = @{ name="telegram-bot";        group="SPECIALISTS";  desc="Telegram bot specialist" }
    16 = @{ name="n8n-workflow";        group="SPECIALISTS";  desc="n8n automation" }
    17 = @{ name="debugger";            group="SPECIALISTS";  desc="investigate bugs" }
    18 = @{ name="test-writer";         group="SPECIALISTS";  desc="write tests" }
}

Write-Output ""
Write-Output " ================================"
Write-Output "  ag_ai - Agent Launcher"
Write-Output " ================================"
Write-Output ""

$currentGroup = ""
foreach ($key in $agents.Keys) {
    $a = $agents[$key]
    if ($a.group -ne $currentGroup) {
        Write-Output ""
        Write-Output " --- $($a.group) ---"
        $currentGroup = $a.group
    }
    Write-Output (" {0,2})  {1,-28} {2}" -f $key, $a.name, $a.desc)
}
Write-Output ""
Write-Output "  0)  no agent (default Build mode)"
Write-Output ""
$choice = Read-Host "  Choose (0-18)"

if ($choice -eq "0" -or $choice -eq "") {
    Write-Output "  Starting OpenCode in default Build mode..."
    if ($ProjectPath) { opencode $ProjectPath } else { opencode }
}
elseif ($agents.ContainsKey([int]$choice)) {
    $agent = $agents[[int]$choice].name
    $task  = Read-Host "  What do you want to do?"
    $prompt = "use $agent agent to $task"
    Write-Output ""
    Write-Output "  Starting: $prompt"
    if ($ProjectPath) { opencode run $prompt $ProjectPath } else { opencode run $prompt }
}
else {
    Write-Output "  Invalid choice."
}
