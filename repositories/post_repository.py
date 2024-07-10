from utils.database import get_db
from utils.helpers import dict_from_row

class PostRepository:
    def add_post(self, user_id, content):
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO Post (user_id, content) VALUES (%s, %s)"
        cursor.execute(query, (user_id, content))
        db.commit()
        return cursor.lastrowid

    def update_post(self, post_id, content):
        db = get_db()
        cursor = db.cursor()
        query = "UPDATE Post SET content = %s WHERE id = %s"
        cursor.execute(query, (content, post_id))
        db.commit()

    def delete_post(self, post_id):
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM Post WHERE id = %s"
        cursor.execute(query, (post_id,))
        db.commit()

    def get_post(self, post_id):
        db = get_db()
        cursor = db.cursor()
        query = """
            SELECT p.*, u.username as author_username, u.email as author_email 
            FROM Post p 
            JOIN User u ON p.user_id = u.id 
            WHERE p.id = %s
        """
        cursor.execute(query, (post_id,))
        row = cursor.fetchone()
        return dict_from_row(row, cursor)

    def get_like_count(self, post_id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT COUNT(*) as like_count FROM `Like` WHERE post_id = %s"
        cursor.execute(query, (post_id,))
        row = cursor.fetchone()
        return row[0]

    def get_share_count(self, post_id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT COUNT(*) as share_count FROM Share WHERE post_id = %s"
        cursor.execute(query, (post_id,))
        row = cursor.fetchone()
        return row[0]

    def get_all_posts(self):
        db = get_db()
        cursor = db.cursor()
        query = """
            SELECT p.*, u.username as author_username, u.email as author_email,
                   (SELECT COUNT(*) FROM `Like` WHERE post_id = p.id) as like_count,
                   (SELECT COUNT(*) FROM Share WHERE post_id = p.id) as share_count
            FROM Post p 
            JOIN User u ON p.user_id = u.id 
            ORDER BY p.created_at DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return [dict_from_row(row, cursor) for row in rows]
