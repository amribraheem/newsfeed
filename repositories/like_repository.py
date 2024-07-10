from utils.database import get_db


class LikeRepository:
    def add_like(self, post_id, user_id):
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO `Like` (post_id, user_id) VALUES (%s, %s)"
        cursor.execute(query, (post_id, user_id))
        db.commit()
        return cursor.lastrowid

    def get_likes_by_post(self, post_id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM `Like` WHERE post_id = %s"
        cursor.execute(query, (post_id,))
        return cursor.fetchall()
