from flask import Blueprint, request, jsonify
from services.share_service import ShareService

share_bp = Blueprint('share', __name__)
share_service = ShareService()

@share_bp.route('', methods=['POST'])
def add_share():
    data = request.json
    result = share_service.add_share(data)
    return jsonify(result), 201 if result['success'] else 400

@share_bp.route('/post/<int:post_id>', methods=['GET'])
def get_shares_by_post(post_id):
    result = share_service.get_shares_by_post(post_id)
    return jsonify(result), 200 if result['success'] else 404
