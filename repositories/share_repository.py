from utils.database import get_db


class ShareRepository:
    def add_share(self, post_id, user_id):
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO Share (post_id, user_id) VALUES (%s, %s)"
        cursor.execute(query, (post_id, user_id))
        db.commit()
        return cursor.lastrowid

    def get_shares_by_post(self, post_id):
        db = get_db()
        cursor = db.cursor()
        query = "SELECT * FROM Share WHERE post_id = %s"
        cursor.execute(query, (post_id,))
        return cursor.fetchall()
