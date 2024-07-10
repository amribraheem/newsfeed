from utils.database import get_db


class CommentRepository:
    def add_comment(self, post_id, user_id, content):
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO Comment (post_id, user_id, content) VALUES (%s, %s, %s)"
        cursor.execute(query, (post_id, user_id, content))
        db.commit()
        return cursor.lastrowid

    def get_comments_by_post(self, post_id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM Comment WHERE post_id = %s"
        cursor.execute(query, (post_id,))
        return cursor.fetchall()
