from utils.database import get_db
from utils.helpers import dict_from_row

class LikeRepository:
    def add_like(self, post_id, user_id):
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO `Like` (post_id, user_id) VALUES (%s, %s)"
        cursor.execute(query, (post_id, user_id))
        db.commit()
        return cursor.lastrowid

    def delete_like(self, like_id):
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM `Like` WHERE id = %s"
        cursor.execute(query, (like_id,))
        db.commit()

    def get_like(self, like_id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM `Like` WHERE id = %s"
        cursor.execute(query, (like_id,))
        row = cursor.fetchone()
        return dict_from_row(row, cursor)

    def get_likes_by_post(self, post_id):
        db = get_db()
        cursor = db.cursor()
        query = """
            SELECT l.*, u.username as user_username, u.email as user_email 
            FROM `Like` l 
            JOIN User u ON l.user_id = u.id 
            WHERE l.post_id = %s
        """
        cursor.execute(query, (post_id,))
        rows = cursor.fetchall()
        return [dict_from_row(row, cursor) for row in rows]
