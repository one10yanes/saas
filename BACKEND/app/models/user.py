from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def set_password(self, password):
        print(f"Estableciendo contraseña para usuario {self.email}") # Debug
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')
        print(f"Hash generado: {self.password_hash}") # Debug

    def check_password(self, password):
        print(f"Verificando contraseña para usuario {self.email}") # Debug
        if not self.password_hash:
            print("No hay hash de contraseña almacenado") # Debug
            return False
        print(f"Hash almacenado: {self.password_hash}") # Debug
        result = check_password_hash(self.password_hash, password)
        print(f"Resultado de verificación: {result}") # Debug
        return result

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_active': self.is_active
        } 