from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    from blueprints.api import api_bp
    
    app.register_blueprint(api_bp, url_prefix='/api')
    
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