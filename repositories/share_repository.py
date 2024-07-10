from utils.database import get_db
from utils.helpers import dict_from_row

class ShareRepository:
    def add_share(self, post_id, user_id):
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO Share (post_id, user_id) VALUES (%s, %s)"
        cursor.execute(query, (post_id, user_id))
        db.commit()
        return cursor.lastrowid

    def delete_share(self, share_id):
        db = get_db()
        cursor = db.cursor()
        query = "DELETE FROM Share WHERE id = %s"
        cursor.execute(query, (share_id,))
        db.commit()

    def get_share(self, share_id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM Share WHERE id = %s"
        cursor.execute(query, (share_id,))
        row = cursor.fetchone()
        return dict_from_row(row, cursor)

    def get_shares_by_post(self, post_id):
        db = get_db()
        cursor = db.cursor()
        query = """
            SELECT s.*, u.username as user_username, u.email as user_email 
            FROM Share s 
            JOIN User u ON s.user_id = u.id 
            WHERE s.post_id = %s
        """
        cursor.execute(query, (post_id,))
        rows = cursor.fetchall()
        return [dict_from_row(row, cursor) for row in rows]
