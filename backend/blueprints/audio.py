from flask import Blueprint, request, jsonify, current_app
import os
from werkzeug.utils import secure_filename

audio_bp = Blueprint('audio', __name__)

def allowed_audio_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_AUDIO_EXTENSIONS']

@audio_bp.route('/upload', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_audio_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['AUDIO_FOLDER'], filename)
        file.save(file_path)
        
        return jsonify({
            'message': 'Audio file uploaded successfully',
            'filename': filename,
            'path': file_path
        }), 200
    
    return jsonify({'error': 'Invalid audio file type'}), 400

@audio_bp.route('/record', methods=['POST'])
def record_audio():
    return jsonify({'message': 'Audio recording endpoint - to be implemented'}), 501

@audio_bp.route('/analyze', methods=['POST'])
def analyze_pronunciation():
    return jsonify({'message': 'Pronunciation analysis endpoint - to be implemented'}), 501