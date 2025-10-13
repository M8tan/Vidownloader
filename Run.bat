@echo off
cd /d %~dp0

call venv\scripts\activate.bat
python Full.py
cmd /k
