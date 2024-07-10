from flask import Blueprint, request, jsonify
from services.like_service import LikeService

like_bp = Blueprint('like', __name__)
like_service = LikeService()

@like_bp.route('', methods=['POST'])
def add_like():
    data = request.json
    result = like_service.add_like(data)
    return jsonify(result), 201 if result['success'] else 400

@like_bp.route('/post/<int:post_id>', methods=['GET'])
def get_likes_by_post(post_id):
    result = like_service.get_likes_by_post(post_id)
    return jsonify(result), 200 if result['success'] else 404
