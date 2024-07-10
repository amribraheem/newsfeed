from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.share_service import ShareService

share_bp = Blueprint('share', __name__)
share_service = ShareService()

@share_bp.route('', methods=['POST'])
@jwt_required()
def add_share():
    data = request.json
    current_user = get_jwt_identity()
    result = share_service.add_share(current_user['id'], data)
    return jsonify(result), 201 if result['success'] else 400

@share_bp.route('/<int:share_id>', methods=['DELETE'])
@jwt_required()
def delete_share(share_id):
    current_user = get_jwt_identity()
    result = share_service.delete_share(share_id, current_user['id'])
    return jsonify(result), 200 if result['success'] else 400

@share_bp.route('/post/<int:post_id>', methods=['GET'])
def get_shares_by_post(post_id):
    result = share_service.get_shares_by_post(post_id)
    return jsonify(result), 200
