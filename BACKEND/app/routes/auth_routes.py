from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return {'error': 'Email y contraseña son requeridos'}, 400
    
    return AuthService.register(data['email'], data['password'])

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('email') or not data.get('password'):
        return {'error': 'Email y contraseña son requeridos'}, 400
    
    result, status_code = AuthService.login(data['email'], data['password'])
    return jsonify(result), status_code 