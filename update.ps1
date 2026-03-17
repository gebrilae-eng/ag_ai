# ag_ai - Update Script (PowerShell)
$AgAiDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host ""
Write-Host " ag_ai - Force Update"
Write-Host " ===================="
Write-Host " Location: $AgAiDir"
Write-Host ""

Set-Location $AgAiDir

Write-Host "Fetching latest from GitHub..."
git fetch origin

Write-Host "Resetting to latest..."
git reset --hard origin/main

Write-Host ""
Write-Host " Done! ag_ai is now up to date."
Write-Host ""
