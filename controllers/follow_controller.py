from flask import Blueprint, request, jsonify
from services.follow_service import FollowService

follow_bp = Blueprint('follow', __name__)
follow_service = FollowService()

@follow_bp.route('', methods=['POST'])
def add_follow():
    data = request.json
    result = follow_service.add_follow(data)
    return jsonify(result), 201 if result['success'] else 400

@follow_bp.route('/user/<int:user_id>/followers', methods=['GET'])
def get_followers(user_id):
    result = follow_service.get_followers(user_id)
    return jsonify(result), 200 if result['success'] else 404
