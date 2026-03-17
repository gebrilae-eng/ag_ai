# ag_ai - Install Script (PowerShell)
param(
    [string]$ProjectPath = ""
)

$AgAiDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host ""
Write-Host " ag_ai - Update and Install"
Write-Host " ==========================="
Write-Host " ag_ai location: $AgAiDir"
Write-Host ""

Set-Location $AgAiDir

Write-Host "[1/3] Pulling latest from GitHub..."
git fetch origin
git reset --hard origin/main
Write-Host ""

Write-Host "[2/3] Running setup..."
if ($ProjectPath -eq "") {
    python "$AgAiDir\setup_ai.py"
} else {
    python "$AgAiDir\setup_ai.py" $ProjectPath
}

Write-Host ""
Write-Host "[3/3] Done!"
Read-Host "Press Enter to continue"
