from flask import Flask, send_from_directory
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint

from controllers.auth_controller import auth_bp
from controllers.post_controller import post_bp
from controllers.user_controller import user_bp
from controllers.comment_controller import comment_bp
from controllers.like_controller import like_bp
from controllers.share_controller import share_bp
from controllers.follow_controller import follow_bp
from utils.database import initialize_db, create_tables

app = Flask(__name__)
app.config.from_object('config.Config')

initialize_db(app)
jwt = JWTManager(app)

with app.app_context():
    create_tables()

app.register_blueprint(post_bp, url_prefix='/posts')
app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(comment_bp, url_prefix='/comments')
app.register_blueprint(like_bp, url_prefix='/likes')
app.register_blueprint(share_bp, url_prefix='/shares')
app.register_blueprint(follow_bp, url_prefix='/follows')
app.register_blueprint(auth_bp, url_prefix='/auth')


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Newsfeed API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(debug=True)
