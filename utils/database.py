from flask_mysqldb import MySQL
import mariadb
from mariadb import Error

mysql = MySQL()


def initialize_db(app):
    mysql.init_app(app)


def get_db():
    return mysql.connection


def create_tables():
    db = None
    try:
        db = mariadb.connect(
            host='localhost',
            user='root',
            password='admin'
        )
        cursor = db.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS newsfeed_app")
        cursor.execute("USE newsfeed_app")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL UNIQUE,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Post (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES User(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Comment (
            id INT AUTO_INCREMENT PRIMARY KEY,
            post_id INT NOT NULL,
            user_id INT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (post_id) REFERENCES Post(id),
            FOREIGN KEY (user_id) REFERENCES User(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS `Like` (
            id INT AUTO_INCREMENT PRIMARY KEY,
            post_id INT NOT NULL,
            user_id INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (post_id) REFERENCES Post(id),
            FOREIGN KEY (user_id) REFERENCES User(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Share (
            id INT AUTO_INCREMENT PRIMARY KEY,
            post_id INT NOT NULL,
            user_id INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (post_id) REFERENCES Post(id),
            FOREIGN KEY (user_id) REFERENCES User(id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Follow (
            id INT AUTO_INCREMENT PRIMARY KEY,
            follower_id INT NOT NULL,
            followed_id INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (follower_id) REFERENCES User(id),
            FOREIGN KEY (followed_id) REFERENCES User(id)
        )
        """)

        db.commit()
    except Error as err:
        print(f"Error: {err}")
    finally:
        if db:
            db.close()
