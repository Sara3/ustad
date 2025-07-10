from flask import Blueprint, request, jsonify

text_bp = Blueprint('text', __name__)

@text_bp.route('/process', methods=['POST'])
def process_text():
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    
    text = data['text']
    
    # Basic text processing - to be enhanced with Gemma model
    processed_text = {
        'original': text,
        'word_count': len(text.split()),
        'sentences': text.split('.'),
        'words': text.split()
    }
    
    return jsonify(processed_text)

@text_bp.route('/ocr', methods=['POST'])
def extract_text_from_image():
    return jsonify({'message': 'OCR text extraction - to be implemented with Gemma model'}), 501

@text_bp.route('/tts', methods=['POST'])
def text_to_speech():
    return jsonify({'message': 'Text-to-speech - to be implemented'}), 501