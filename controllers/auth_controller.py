from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    result = auth_service.register_user(data['username'], data['email'], data['password'])
    return jsonify(result), 201 if result['success'] else 400


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    result = auth_service.authenticate_user(data['username'], data['password'])
    return jsonify(result), 200 if result['success'] else 401


@auth_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify({"access_token": new_access_token}), 200
