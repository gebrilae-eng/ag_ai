# ag_ai - Update Script (PowerShell)
$AgAiDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Output ""
Write-Output " ag_ai - Update"
Write-Output " ==============="
Write-Output " Location: $AgAiDir"
Write-Output ""

Set-Location $AgAiDir

Write-Output "[1/2] Fetching latest from GitHub..."
git fetch origin
git reset --hard origin/main

Write-Output ""
Write-Output "[2/2] Done! ag_ai is now up to date."
Write-Output ""
Write-Output " Latest changes:"
Get-Content "$AgAiDir\CHANGELOG.md" -TotalCount 15
Write-Output ""
