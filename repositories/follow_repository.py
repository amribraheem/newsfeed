from utils.database import get_db
from utils.helpers import dict_from_row

class FollowRepository:
    def add_follow(self, follower_id, followed_id):
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO Follow (follower_id, followed_id) VALUES (%s, %s)"
        cursor.execute(query, (follower_id, followed_id))
        db.commit()
        return cursor.lastrowid

    def delete_follow(self, follow_id):
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM Follow WHERE id = %s"
        cursor.execute(query, (follow_id,))
        db.commit()

    def get_follow(self, follow_id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM Follow WHERE id = %s"
        cursor.execute(query, (follow_id,))
        row = cursor.fetchone()
        return dict_from_row(row, cursor)

    def get_followers(self, user_id):
        db = get_db()
        cursor = db.cursor()
        query = """
            SELECT f.*, u.username as follower_username, u.email as follower_email 
            FROM Follow f 
            JOIN User u ON f.follower_id = u.id 
            WHERE f.followed_id = %s
        """
        cursor.execute(query, (user_id,))
        rows = cursor.fetchall()
        return [dict_from_row(row, cursor) for row in rows]
