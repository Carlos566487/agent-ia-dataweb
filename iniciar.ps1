$pasta = "c:\Agentes\agent-ia-dataweb-main"
Set-Location $pasta

$existente = Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue
if ($existente) {
    Write-Host "O servidor ja esta em execucao na porta 8000." -ForegroundColor Green
} else {
    Write-Host "Iniciando servidor DataWeb na porta 8000..." -ForegroundColor Cyan
    Start-Process -FilePath "C:\Python314\python.exe" -ArgumentList "index.py", "servir", "--porta", "8000" -WorkingDirectory $pasta
    Start-Sleep -Seconds 6
}

Start-Process "http://127.0.0.1:8000"
Write-Host "Pronto! Aplicativo aberto em http://127.0.0.1:8000" -ForegroundColor Green
