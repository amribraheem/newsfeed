from flask import Flask
from utils.database import initialize_db, create_tables

app = Flask(__name__)
app.config.from_object('config.Config')

initialize_db(app)
create_tables()

if __name__ == '__main__':
    app.run(debug=True)
