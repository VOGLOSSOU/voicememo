from flask import Flask, request, jsonify
from flask_cors import CORS
import whisper
import os
import tempfile
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Load Whisper model (using base model for balance between speed and accuracy)
# Options: tiny, base, small, medium, large
print("🔄 Chargement du modèle Whisper...")
model = whisper.load_model("base")
print("✅ Modèle Whisper chargé !")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    """
    Endpoint pour transcrire l'audio envoyé depuis le frontend
    """
    try:
        if 'audio' not in request.files:
            return jsonify({
                'success': False,
                'error': 'Aucun fichier audio fourni'
            }), 400
        
        audio_file = request.files['audio']
        
        # Create temporary file to save the audio
        with tempfile.NamedTemporaryFile(delete=False, suffix='.webm') as temp_audio:
            audio_file.save(temp_audio.name)
            temp_path = temp_audio.name
        
        print(f"📝 Transcription en cours... ({datetime.now().strftime('%H:%M:%S')})")
        
        # Transcribe with Whisper
        result = model.transcribe(
            temp_path,
            language='fr',  # French language
            fp16=False  # Use FP32 for better compatibility
        )
        
        # Clean up temp file
        os.unlink(temp_path)
        
        transcript = result['text'].strip()
        
        print(f"✅ Transcription terminée : {len(transcript)} caractères")
        
        return jsonify({
            'success': True,
            'transcript': transcript,
            'language': result.get('language', 'fr')
        })
    
    except Exception as e:
        print(f"❌ Erreur lors de la transcription : {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint
    """
    return jsonify({
        'status': 'ok',
        'model': 'whisper-base',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("="*50)
    print("🎙️  VoiceMemo Backend Server")
    print("="*50)
    print("📍 Serveur démarré sur http://localhost:5000")
    print("🔊 Prêt à transcrire vos notes vocales !")
    print("="*50)
    app.run(debug=True, host='0.0.0.0', port=5000)