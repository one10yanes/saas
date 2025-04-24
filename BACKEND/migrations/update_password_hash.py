from app import create_app, db
from app.models.user import User

def update_password_hash_field():
    app = create_app()
    with app.app_context():
        # Verificar si la tabla existe
        if not db.engine.dialect.has_table(db.engine, 'user'):
            print("Creando tabla de usuarios...")
            db.create_all()
            return
        
        # Intentar modificar la columna password_hash
        try:
            db.engine.execute('ALTER TABLE user MODIFY COLUMN password_hash VARCHAR(256)')
            print("Campo password_hash actualizado correctamente")
        except Exception as e:
            print(f"Error al actualizar el campo: {str(e)}")
            # Si falla, intentamos recrear la tabla
            db.drop_all()
            db.create_all()
            print("Base de datos recreada")

if __name__ == '__main__':
    update_password_hash_field() 