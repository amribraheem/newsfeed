from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.post_service import PostService

post_bp = Blueprint('post', __name__)
post_service = PostService()


@post_bp.route('', methods=['POST'])
@jwt_required()
def add_post():
    data = request.json
    current_user = get_jwt_identity()
    result = post_service.add_post(current_user['id'], data)
    return jsonify(result), 201 if result['success'] else 400


@post_bp.route('/<int:post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    data = request.json
    result = post_service.update_post(post_id, data)
    return jsonify(result), 200 if result['success'] else 400


@post_bp.route('/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    result = post_service.delete_post(post_id)
    return jsonify(result), 200 if result['success'] else 400


@post_bp.route('/<int:post_id>', methods=['GET'])
@jwt_required()
def get_post(post_id):
    result = post_service.get_post(post_id)
    return jsonify(result), 200 if result['success'] else 404
