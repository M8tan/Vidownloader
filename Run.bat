@echo off
cd /d %~dp0

call venv\scripts\activate.bat
title Vidownloader
cls
python Full.py
cmd /k
