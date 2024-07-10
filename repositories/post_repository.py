from utils.database import get_db


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
        query = "SELECT * FROM Post WHERE id = %s"
        cursor.execute(query, (post_id,))
        return cursor.fetchone()
