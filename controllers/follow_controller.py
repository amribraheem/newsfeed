from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.follow_service import FollowService

follow_bp = Blueprint('follow', __name__)
follow_service = FollowService()

@follow_bp.route('', methods=['POST'])
@jwt_required()
def add_follow():
    data = request.json
    current_user = get_jwt_identity()
    result = follow_service.add_follow(current_user['id'], data)
    return jsonify(result), 201 if result['success'] else 400

@follow_bp.route('/<int:follow_id>', methods=['DELETE'])
@jwt_required()
def delete_follow(follow_id):
    current_user = get_jwt_identity()
    result = follow_service.delete_follow(follow_id, current_user['id'])
    return jsonify(result), 200 if result['success'] else 400

@follow_bp.route('/user/<int:user_id>/followers', methods=['GET'])
def get_followers(user_id):
    result = follow_service.get_followers(user_id)
    return jsonify(result), 200 if result['success'] else 404
