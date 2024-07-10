from utils.database import get_db


class UserRepository:
    def add_user(self, username, email, password):
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO User (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, password))
        db.commit()
        return cursor.lastrowid

    def get_user(self, user_id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM User WHERE id = %s"
        cursor.execute(query, (user_id,))
        return cursor.fetchone()
