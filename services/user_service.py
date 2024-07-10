from repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def add_user(self, data):
        try:
            user_id = self.user_repository.add_user(data['username'], data['email'], data['password'])
            return {"success": True, "user_id": user_id}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_user(self, user_id):
        try:
            user = self.user_repository.get_user(user_id)
            if user:
                return {"success": True, "user": user}
            return {"success": False, "error": "User not found"}
        except Exception as e:
            return {"success": False, "error": str(e)}
