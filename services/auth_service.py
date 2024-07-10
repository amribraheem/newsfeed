import bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token
from repositories.user_repository import UserRepository

class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, username, email, password):
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        try:
            user_id = self.user_repository.add_user(username, email, hashed_password)
            access_token = create_access_token(identity={'id': user_id, 'username': username, 'email': email})
            refresh_token = create_refresh_token(identity={'id': user_id, 'username': username, 'email': email})
            return {
                "success": True,
                "user": {"id": user_id, "username": username, "email": email},
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

    def authenticate_user(self, username, password):
        user = self.user_repository.get_user_by_username(username)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            access_token = create_access_token(identity={'id': user['id'], 'username': username, 'email': user['email']})
            refresh_token = create_refresh_token(identity={'id': user['id'], 'username': username, 'email': user['email']})
            return {
                "success": True,
                "user": {"id": user['id'], "username": user['username'], "email": user['email']},
                "access_token": access_token,
                "refresh_token": refresh_token
            }
        return {"success": False, "error": "Invalid credentials"}
