#!/bin/bash

# VoiceMemo Launcher Script
# Ce script lance le serveur backend et ouvre l'application dans le navigateur

echo "=================================================="
echo "🎙️  VoiceMemo - Démarrage de l'application"
echo "=================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé !"
    echo "   Installez Python depuis https://python.org"
    exit 1
fi

echo "✅ Python détecté : $(python3 --version)"
echo ""

# Check if dependencies are installed
echo "🔍 Vérification des dépendances..."
if ! python3 -c "import flask" 2>/dev/null; then
    echo "⚠️  Dépendances manquantes. Installation..."
    pip install -r requirements.txt
    echo ""
fi

echo "✅ Dépendances OK"
echo ""

# Start backend server
echo "🚀 Démarrage du serveur backend..."
echo "   URL: http://localhost:5000"
echo ""
echo "📝 Ouvrez index.html dans votre navigateur"
echo "   Ou utilisez: python3 -m http.server 8000"
echo ""
echo "=================================================="
echo "Appuyez sur Ctrl+C pour arrêter le serveur"
echo "=================================================="
echo ""

python3 app.py