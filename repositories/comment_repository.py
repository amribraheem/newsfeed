from utils.database import get_db
from utils.helpers import dict_from_row

class CommentRepository:
    def add_comment(self, post_id, user_id, content):
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO Comment (post_id, user_id, content) VALUES (%s, %s, %s)"
        cursor.execute(query, (post_id, user_id, content))
        db.commit()
        return cursor.lastrowid

    def update_comment(self, comment_id, content):
        db = get_db()
        cursor = db.cursor()
        query = "UPDATE Comment SET content = %s WHERE id = %s"
        cursor.execute(query, (content, comment_id))
        db.commit()

    def delete_comment(self, comment_id):
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM Comment WHERE id = %s"
        cursor.execute(query, (comment_id,))
        db.commit()

    def get_comment(self, comment_id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM Comment WHERE id = %s"
        cursor.execute(query, (comment_id,))
        row = cursor.fetchone()
        return dict_from_row(row, cursor)

    def get_comments_by_post(self, post_id):
        db = get_db()
        cursor = db.cursor()
        query = """
            SELECT c.*, u.username as author_username, u.email as author_email 
            FROM Comment c 
            JOIN User u ON c.user_id = u.id 
            WHERE c.post_id = %s
            ORDER BY c.created_at DESC
        """
        cursor.execute(query, (post_id,))
        rows = cursor.fetchall()
        return [dict_from_row(row, cursor) for row in rows]
