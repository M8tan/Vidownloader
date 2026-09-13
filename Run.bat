@echo off
cd /d %~dp0

call venv\scripts\activate.bat
title Vidownloader
cls
python main.py
timeout /t 3 /nobreak>nul
exit
