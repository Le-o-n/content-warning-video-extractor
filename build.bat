@echo off
call ./install_requirements.bat
pyinstaller --onefile --distpath ./build main.py
pause