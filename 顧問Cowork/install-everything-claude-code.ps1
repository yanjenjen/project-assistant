# install-everything-claude-code.ps1
$ErrorActionPreference = "Stop"
$repo = "https://github.com/affaan-m/everything-claude-code.git"
$cloneDir = "$env:TEMP\everything-claude-code"
$rulesDir = "$env:USERPROFILE\.claude\rules"

Write-Host "=== Step 1: Check git ===" -ForegroundColor Cyan
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: git not found. Install from https://git-scm.com/download/win" -ForegroundColor Red
    pause
    exit 1
}
Write-Host "OK: $(git --version)"

Write-Host "=== Step 2: Clone repo ===" -ForegroundColor Cyan
if (Test-Path $cloneDir) {
    Write-Host "Updating existing clone..."
    git -C $cloneDir pull
} else {
    git clone $repo $cloneDir
}
Write-Host "OK: Repo ready at $cloneDir"

Write-Host "=== Step 3: Copy rules to $rulesDir ===" -ForegroundColor Cyan
if (-not (Test-Path $rulesDir)) {
    New-Item -ItemType Directory -Path $rulesDir -Force | Out-Null
}
Copy-Item "$cloneDir\rules\*" $rulesDir -Recurse -Force
Write-Host "OK: Rules copied"

Write-Host ""
Write-Host "=== DONE ===" -ForegroundColor Green
Write-Host "Rules installed. Now open a terminal, run 'claude', then type:" -ForegroundColor White
Write-Host "  /plugin marketplace add affaan-m/everything-claude-code" -ForegroundColor Yellow
Write-Host "  /plugin install everything-claude-code@everything-claude-code" -ForegroundColor Yellow
Write-Host ""
pause
