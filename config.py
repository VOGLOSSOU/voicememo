# VoiceMemo Configuration File
# Fichier de configuration pour personnaliser VoiceMemo

# Modèle Whisper à utiliser
# Options: tiny, base, small, medium, large
# Plus le modèle est grand, plus il est précis mais lent
WHISPER_MODEL = "base"

# Langue par défaut pour la transcription
# Options: fr (français), en (anglais), es (espagnol), de (allemand), etc.
# Voir: https://github.com/openai/whisper#available-models-and-languages
DEFAULT_LANGUAGE = "fr"

# Port du serveur backend
SERVER_PORT = 5000

# Host du serveur (0.0.0.0 = accessible depuis le réseau local)
SERVER_HOST = "0.0.0.0"

# Mode debug (True = plus de logs, False = mode production)
DEBUG_MODE = True

# Taille maximale des fichiers audio (en Mo)
MAX_AUDIO_SIZE_MB = 50

# Timeout pour la transcription (en secondes)
TRANSCRIPTION_TIMEOUT = 300

# Format audio acceptés
ALLOWED_AUDIO_FORMATS = ['.wav', '.mp3', '.m4a', '.webm', '.ogg']

# Activer/désactiver les logs détaillés
VERBOSE_LOGGING = True

# Configuration CORS (pour autoriser d'autres domaines)
CORS_ORIGINS = "*"  # "*" = tous les domaines (pour dev local)

# Répertoire temporaire pour les fichiers audio
TEMP_DIR = "/tmp"

# ====================================================================
# NOTES D'UTILISATION :
# ====================================================================
# Pour utiliser ce fichier, importez-le dans app.py :
#
#   from config import WHISPER_MODEL, DEFAULT_LANGUAGE, SERVER_PORT
#   
#   model = whisper.load_model(WHISPER_MODEL)
#   app.run(port=SERVER_PORT)
#
# ====================================================================