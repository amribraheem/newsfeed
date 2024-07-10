from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.like_service import LikeService

like_bp = Blueprint('like', __name__)
like_service = LikeService()

@like_bp.route('', methods=['POST'])
@jwt_required()
def add_like():
    data = request.json
    current_user = get_jwt_identity()
    result = like_service.add_like(current_user['id'], data)
    return jsonify(result), 201 if result['success'] else 400

@like_bp.route('/<int:like_id>', methods=['DELETE'])
@jwt_required()
def delete_like(like_id):
    current_user = get_jwt_identity()
    result = like_service.delete_like(like_id, current_user['id'])
    return jsonify(result), 200 if result['success'] else 400

@like_bp.route('/post/<int:post_id>', methods=['GET'])
def get_likes_by_post(post_id):
    result = like_service.get_likes_by_post(post_id)
    return jsonify(result), 200 if result['success'] else 404
