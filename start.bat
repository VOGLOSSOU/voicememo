@echo off
REM VoiceMemo Launcher Script for Windows
REM Ce script lance le serveur backend

echo ==================================================
echo 🎙️  VoiceMemo - Demarrage de l'application
echo ==================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python n'est pas installe !
    echo    Installez Python depuis https://python.org
    pause
    exit /b 1
)

echo ✅ Python detecte
echo.

echo 🔍 Verification des dependances...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Dependances manquantes. Installation...
    pip install -r requirements.txt
    echo.
)

echo ✅ Dependances OK
echo.

echo 🚀 Demarrage du serveur backend...
echo    URL: http://localhost:5000
echo.
echo 📝 Ouvrez index.html dans votre navigateur
echo    Ou utilisez: python -m http.server 8000
echo.
echo ==================================================
echo Appuyez sur Ctrl+C pour arreter le serveur
echo ==================================================
echo.

python app.py
pause