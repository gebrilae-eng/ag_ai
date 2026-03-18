# ag_ai - Install Script (PowerShell)
param(
    [string]$ProjectPath = ""
)

$AgAiDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Output ""
Write-Output " ag_ai - Install"
Write-Output " ================"
Write-Output " ag_ai location: $AgAiDir"
Write-Output ""

Write-Output "[1/2] Running setup..."
if ($ProjectPath -eq "") {
    python "$AgAiDir\setup_ai.py"
} else {
    python "$AgAiDir\setup_ai.py" $ProjectPath
}

Write-Output ""
Write-Output "[2/2] Done!"
Write-Output ""
Write-Output " Tip: to update ag_ai itself run update.ps1"
Read-Host "Press Enter to continue"
