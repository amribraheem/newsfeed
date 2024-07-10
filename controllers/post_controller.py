from flask import Blueprint, request, jsonify
from services.post_service import PostService

post_bp = Blueprint('post', __name__)
post_service = PostService()

@post_bp.route('', methods=['POST'])
def add_post():
    data = request.json
    result = post_service.add_post(data)
    return jsonify(result), 201 if result['success'] else 400

@post_bp.route('/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    data = request.json
    result = post_service.update_post(post_id, data)
    return jsonify(result), 200 if result['success'] else 400

@post_bp.route('/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    result = post_service.delete_post(post_id)
    return jsonify(result), 200 if result['success'] else 400

@post_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    result = post_service.get_post(post_id)
    return jsonify(result), 200 if result['success'] else 404
