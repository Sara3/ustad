import os
from pathlib import Path

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # File upload settings
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    
    # Audio settings
    AUDIO_FOLDER = os.path.join(os.path.dirname(__file__), 'audio')
    ALLOWED_AUDIO_EXTENSIONS = {'wav', 'mp3', 'ogg', 'flac'}
    
    # Database settings
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'app.db')
    
    # Ollama settings
    OLLAMA_BASE_URL = 'http://localhost:11434'
    GEMMA_MODEL = 'gemma2:2b'
    
    # Create directories if they don't exist
    Path(UPLOAD_FOLDER).mkdir(parents=True, exist_ok=True)
    Path(AUDIO_FOLDER).mkdir(parents=True, exist_ok=True)