from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from travelappbackend.models import User
from travelappbackend.schemas.user import user_schema, users_schema
from travelappbackend.services.user_service import follow_user, get_user_by_id

users_bp = Blueprint('users', __name__)

# Get all users
@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users)), 200

# Get a single user profile
@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(user_schema.dump(user)), 200

# Follow a user
@users_bp.route('/users/<int:user_id>/follow', methods=['POST'])
@jwt_required()
def follow(user_id):
    current_user_id = get_jwt_identity()
    user = follow_user(current_user_id, user_id)
    
    if user:
        return jsonify({"message": f"You are now following {user.username}"}), 200
    return jsonify({"message": "User not found or already followed"}), 400
