from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    from blueprints.api import api_bp
    from blueprints.upload import upload_bp
    from blueprints.audio import audio_bp
    from blueprints.text import text_bp
    
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(upload_bp, url_prefix='/upload')
    app.register_blueprint(audio_bp, url_prefix='/audio')
    app.register_blueprint(text_bp, url_prefix='/text')
    
    @app.route('/')
    def index():
        return jsonify({"message": "English Learning App API"})
    
    @app.route('/health')
    def health():
        return jsonify({"status": "healthy"})
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5001)