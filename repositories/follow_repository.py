from utils.database import get_db


class FollowRepository:
    def add_follow(self, follower_id, followed_id):
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO Follow (follower_id, followed_id) VALUES (%s, %s)"
        cursor.execute(query, (follower_id, followed_id))
        db.commit()
        return cursor.lastrowid

    def get_followers(self, user_id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM Follow WHERE followed_id = %s"
        cursor.execute(query, (user_id,))
        return cursor.fetchall()
