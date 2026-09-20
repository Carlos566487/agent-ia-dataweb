@echo off
cd /d "c:\Agentes\agent-ia-dataweb-main"
start "Agente DataWeb" /min "C:\Python314\python.exe" index.py servir --porta 8000
timeout /t 5 /nobreak >nul
start http://127.0.0.1:8000
