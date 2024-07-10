from utils.database import get_db
from utils.helpers import dict_from_row

class UserRepository:
    def add_user(self, username, email, password):
        try:
            db = get_db()
            cursor = db.cursor()
            query = "INSERT INTO User (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, email, password))
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error: {e}")
            raise e

    def get_user(self, user_id):
        try:
            db = get_db()
            cursor = db.cursor()
            query = "SELECT * FROM User WHERE id = %s"
            cursor.execute(query, (user_id,))
            row = cursor.fetchone()
            return dict_from_row(row, cursor)
        except Exception as e:
            print(f"Error: {e}")
            raise e

    def get_user_by_username(self, username):
        try:
            db = get_db()
            cursor = db.cursor()
            query = "SELECT * FROM User WHERE username = %s"
            cursor.execute(query, (username,))
            row = cursor.fetchone()
            return dict_from_row(row, cursor)
        except Exception as e:
            print(f"Error: {e}")
            raise e
