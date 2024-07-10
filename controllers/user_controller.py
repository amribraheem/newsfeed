from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_bp = Blueprint('user', __name__)
user_service = UserService()

@user_bp.route('', methods=['POST'])
def add_user():
    data = request.json
    result = user_service.add_user(data)
    return jsonify(result), 201 if result['success'] else 400

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    result = user_service.get_user(user_id)
    return jsonify(result), 200 if result['success'] else 404
