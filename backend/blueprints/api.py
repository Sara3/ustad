from flask import Blueprint, jsonify, request

api_bp = Blueprint('api', __name__)

@api_bp.route('/status')
def status():
    return jsonify({"status": "API is running"})

@api_bp.route('/test')
def test():
    return jsonify({"message": "API test endpoint working"})