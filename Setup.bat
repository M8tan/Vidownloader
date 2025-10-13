@echo off
git clone https://github.com/M8tan/Vidownloader.git
cd Vidownloader
python -m venv venv
call venv\scripts\activate.bat
pip install -r requirements.txt
echo Done!
echo Feel free to run the Run.bat file
timeout /t 3 /nobreak>nul