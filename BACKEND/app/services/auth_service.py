from app.models.user import User
from app import db
from flask import jsonify
import jwt
from datetime import datetime, timedelta
import os

class AuthService:
    @staticmethod
    def register(email, password):
        if User.query.filter_by(email=email).first():
            return {'error': 'El email ya está registrado'}, 400
        
        user = User(email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        return {'message': 'Usuario registrado exitosamente'}, 201

    @staticmethod
    def login(email, password):
        print(f"Intentando login con email: {email}") # Debug
        user = User.query.filter_by(email=email).first()
        
        if not user:
            print("Usuario no encontrado") # Debug
            return {'error': 'Email o contraseña inválidos'}, 401
        
        if not user.check_password(password):
            print("Contraseña incorrecta") # Debug
            return {'error': 'Email o contraseña inválidos'}, 401
        
        print("Login exitoso, generando token") # Debug
        token = jwt.encode(
            {
                'user_id': user.id,
                'email': user.email,
                'exp': datetime.utcnow() + timedelta(days=1)
            },
            os.getenv('SECRET_KEY', 'your-secret-key'),
            algorithm='HS256'
        )
        
        user_data = {
            'id': user.id,
            'email': user.email
        }
        
        return {
            'token': token,
            'user': user_data,
            'message': 'Login exitoso'
        }, 200

    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(
                token,
                os.getenv('SECRET_KEY', 'your-secret-key'),
                algorithms=['HS256']
            )
            user = User.query.get(payload['user_id'])
            if not user:
                return None
            return user
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None 