# VoiceMemo - Notes Vocales → Texte

Application web pour enregistrer des notes vocales et les transcrire automatiquement en texte avec Whisper.

##  Fonctionnalités

✅ **Enregistrement audio** depuis le microphone  
✅ **Visualisation en temps réel** de la forme d'onde  
✅ **Transcription automatique** avec Whisper (OpenAI)  
✅ **Sauvegarde locale** des mémos (localStorage)  
✅ **Lecture audio** et édition du texte transcrit  
✅ **Export en TXT** de vos transcriptions  
✅ **Design minimaliste** noir et blanc  
✅ **100% local** - aucune donnée envoyée sur internet  

##  Installation

### Prérequis

- Python 3.8+
- Un navigateur moderne (Chrome, Firefox, Edge)
- Un microphone

### Étape 1 : Installer les dépendances Python

```bash
pip install -r requirements.txt
```

**Note :** L'installation de Whisper peut prendre quelques minutes car il télécharge les modèles nécessaires.

### Étape 2 : Lancer le serveur backend

```bash
python app.py
```

Le serveur démarrera sur `http://localhost:5000`

### Étape 3 : Ouvrir l'application

Ouvrez simplement le fichier `index.html` dans votre navigateur ou utilisez un serveur local :

```bash
# Avec Python
python -m http.server 8000

# Puis ouvrir http://localhost:8000
```

##  Utilisation

1. **Enregistrer** : Cliquez sur le bouton 🎙️ pour commencer l'enregistrement
2. **Arrêter** : Cliquez à nouveau sur ⏹️ pour arrêter
3. **Sauvegarder** : Cliquez sur "💾 Sauvegarder et Transcrire"
4. **Visualiser** : Vos mémos apparaissent dans la liste en bas
5. **Éditer** : Cliquez sur un mémo pour écouter et modifier le texte
6. **Exporter** : Téléchargez la transcription en fichier TXT

##  Architecture

```
VoiceMemo/
├── index.html          # Frontend (interface utilisateur)
├── app.py             # Backend Flask + Whisper
├── requirements.txt   # Dépendances Python
└── README.md         # Documentation
```

### Frontend
- **HTML/CSS/JS** pur (pas de framework)
- **Web Audio API** pour l'enregistrement
- **Canvas API** pour la visualisation
- **localStorage** pour la sauvegarde locale

### Backend
- **Flask** : serveur web Python
- **Whisper** : modèle de transcription OpenAI
- **CORS** : communication frontend ↔ backend

## ⚙️ Configuration

### Changer le modèle Whisper

Dans `app.py`, ligne 12, vous pouvez choisir différents modèles :

```python
model = whisper.load_model("base")  # Par défaut
```

**Options disponibles :**
- `tiny` : Plus rapide, moins précis (~1GB RAM)
- `base` : Bon équilibre (recommandé, ~1GB RAM)
- `small` : Plus précis (~2GB RAM)
- `medium` : Très précis (~5GB RAM)
- `large` : Maximum de précision (~10GB RAM)

### Changer la langue

Dans `app.py`, ligne 38 :

```python
result = model.transcribe(
    temp_path,
    language='fr',  # 'en' pour anglais, 'es' pour espagnol, etc.
    fp16=False
)
```

##  Dépannage

### Le microphone ne fonctionne pas
- Vérifiez les permissions du navigateur
- Testez avec HTTPS ou localhost uniquement
- Vérifiez que votre micro est bien branché

### Erreur "Impossible de contacter le serveur"
- Vérifiez que `python app.py` est bien lancé
- Le serveur doit tourner sur `http://localhost:5000`
- Vérifiez les logs dans la console Python

### La transcription est lente
- Utilisez un modèle plus petit (`tiny` ou `base`)
- Vérifiez que vous n'enregistrez pas des audios trop longs
- Attendez le premier chargement du modèle (peut être long)

### Les mémos disparaissent au refresh
- Vérifiez que vous n'êtes pas en navigation privée
- localStorage peut être désactivé dans certains navigateurs
- Les données sont stockées par domaine/port

##  Personnalisation

### Couleurs
Dans `index.html`, modifiez les variables CSS :

```css
background: #000000;  /* Noir */
color: #FFFFFF;       /* Blanc */
border: 3px solid #000000;
```

### Durée maximale d'enregistrement
Ajoutez cette logique dans la fonction `startRecording()` :

```javascript
const MAX_DURATION = 300; // 5 minutes en secondes
setTimeout(() => {
    if (mediaRecorder.state === 'recording') {
        stopRecording();
    }
}, MAX_DURATION * 1000);
```

##  Format des données

Les mémos sont stockés dans localStorage avec cette structure :

```json
{
  "id": 1707584920000,
  "date": "2024-02-10T14:22:00.000Z",
  "audioUrl": "blob:...",
  "audioBlob": "ArrayBuffer",
  "transcript": "Texte transcrit...",
  "duration": "02:35"
}
```

##  Sécurité & Confidentialité

- ✅ **100% local** : Aucune donnée n'est envoyée sur internet
- ✅ **Pas de compte** : Pas besoin de créer un compte
- ✅ **Pas de tracking** : Aucun analytics ou cookies
- ✅ **Open source** : Code entièrement auditable

##  Technologies utilisées

- **Frontend** : Vanilla JS, Web Audio API, Canvas API
- **Backend** : Python, Flask, OpenAI Whisper
- **Stockage** : localStorage (navigateur)
- **Styling** : CSS pur


##  Contribution

Les contributions sont les bienvenues ! N'hésite pas à :
- Signaler des bugs
- Proposer des améliorations
- Soumettre des pull requests

##  Support

Pour toute question ou problème, ouvre une issue sur le repo.

---

**Fait pour simplifier la prise de notes vocales**