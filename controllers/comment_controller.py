from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.comment_service import CommentService

comment_bp = Blueprint('comment', __name__)
comment_service = CommentService()


@comment_bp.route('', methods=['POST'])
@jwt_required()
def add_comment():
    data = request.json
    current_user = get_jwt_identity()
    result = comment_service.add_comment(current_user['id'], data)
    return jsonify(result), 201 if result['success'] else 400


@comment_bp.route('/<int:comment_id>', methods=['PUT'])
@jwt_required()
def update_comment(comment_id):
    data = request.json
    current_user = get_jwt_identity()
    result = comment_service.update_comment(comment_id, current_user['id'], data)
    return jsonify(result), 200 if result['success'] else 400


@comment_bp.route('/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(comment_id):
    current_user = get_jwt_identity()
    result = comment_service.delete_comment(comment_id, current_user['id'])
    return jsonify(result), 200 if result['success'] else 400


@comment_bp.route('/post/<int:post_id>', methods=['GET'])
def get_comments_by_post(post_id):
    result = comment_service.get_comments_by_post(post_id)
    return jsonify(result), 200 if result['success'] else 404
