from flask import Blueprint, jsonify, request, current_app
import os
import requests
from werkzeug.utils import secure_filename

api_bp = Blueprint('api', __name__)

def allowed_file(filename):
    allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav', 'mp3', 'ogg', 'flac'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@api_bp.route('/status')
def status():
    return jsonify({"status": "API is running"})

@api_bp.route('/process', methods=['POST'])
def process_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400
    
    # Save file temporarily
    filename = secure_filename(file.filename)
    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    
    try:
        # Send to Ollama/Gemma for processing
        with open(file_path, 'rb') as f:
            files = {'file': f}
            
            # Call Ollama API
            ollama_url = f"{current_app.config['OLLAMA_BASE_URL']}/api/generate"
            
            payload = {
                "model": current_app.config['GEMMA_MODEL'],
                "prompt": "Extract all text from this image or audio file. Return only the extracted text, no explanations.",
                "stream": False
            }
            
            response = requests.post(ollama_url, json=payload, files=files)
            
            if response.status_code == 200:
                result = response.json()
                extracted_text = result.get('response', '')
                
                return jsonify({
                    'text': extracted_text,
                    'filename': filename,
                    'status': 'success'
                })
            else:
                return jsonify({'error': 'Failed to process file with Gemma'}), 500
                
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500
    
    finally:
        # Clean up temporary file
        if os.path.exists(file_path):
            os.remove(file_path)