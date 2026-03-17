# ag_ai - Project Setup Wizard (PowerShell)
param(
    [string]$ProjectPath = ""
)

$AgAiDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host ""
Write-Host " ag_ai - Project Setup Wizard"
Write-Host " =============================="
Write-Host ""

if ($ProjectPath -eq "") {
    python "$AgAiDir\wizard.py"
} else {
    python "$AgAiDir\wizard.py" $ProjectPath
}

Read-Host "Press Enter to continue"
