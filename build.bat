@echo off
echo Deleting old build folder...
if exist ".\build\" (
    rmdir /s /q ".\build"
)
echo Building the application...
call ./install_requirements.bat
pyinstaller --onefile --name ContentWarningVideoExtractor --distpath ./build main.py
echo Cleaning up files
del /q *.spec
echo Build and cleanup completed.
pause
