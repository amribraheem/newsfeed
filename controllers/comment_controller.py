from flask import Blueprint, request, jsonify
from services.comment_service import CommentService

comment_bp = Blueprint('comment', __name__)
comment_service = CommentService()

@comment_bp.route('', methods=['POST'])
def add_comment():
    data = request.json
    result = comment_service.add_comment(data)
    return jsonify(result), 201 if result['success'] else 400

@comment_bp.route('/post/<int:post_id>', methods=['GET'])
def get_comments_by_post(post_id):
    result = comment_service.get_comments_by_post(post_id)
    return jsonify(result), 200 if result['success'] else 404
