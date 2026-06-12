$ErrorActionPreference = "Continue"

$logPath = "C:\Users\jenny.lu\Documents\艾創點數位-ERP顧問\05_暫存區\repair_codex_app.log"
$manifest = "C:\Program Files\WindowsApps\OpenAI.Codex_26.527.3686.0_x64__2p2nqsd0c76g0\AppxManifest.xml"
$exe = "C:\Program Files\WindowsApps\OpenAI.Codex_26.527.3686.0_x64__2p2nqsd0c76g0\app\Codex.exe"

function Write-RepairLog {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -LiteralPath $logPath -Value "[$timestamp] $Message"
}

Write-RepairLog "Repair scheduled. Waiting before closing Codex."
Start-Sleep -Seconds 10

Write-RepairLog "Stopping Codex processes."
Get-Process | Where-Object {
    $_.ProcessName -match "^(Codex|codex)$"
} | Stop-Process -Force

Start-Sleep -Seconds 3

Write-RepairLog "Re-registering Appx package."
try {
    Add-AppxPackage -Register $manifest -DisableDevelopmentMode
    Write-RepairLog "Appx registration completed."
} catch {
    Write-RepairLog "Appx registration failed: $($_.Exception.Message)"
}

Start-Sleep -Seconds 2

Write-RepairLog "Starting Codex."
try {
    Start-Process -FilePath $exe
    Write-RepairLog "Codex start command issued."
} catch {
    Write-RepairLog "Codex restart failed: $($_.Exception.Message)"
}
