import jwt
import datetime
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.models import db, User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Check if user already exists
    user = User.query.filter_by(email=data['email']).first()
    if user:
        return jsonify({'message': 'User already exists'}), 409
    
    # Create new user
    new_user = User(email=data['email'], name=data.get('name', ''))
    new_user.set_password(data['password'])
    
    # Save to database
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Find user by email
    user = User.query.filter_by(email=data['email']).first()
    
    if not user or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid credentials'}), 401
    
    # Generate token
    token = jwt.encode(
        {
            'sub': user.id,
            'name': user.name,
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        },
        current_app.config.get('SECRET_KEY', 'dev_key')
    )
    
    return jsonify({'token': token, 'user': {'id': user.id, 'email': user.email, 'name': user.name}}), 200