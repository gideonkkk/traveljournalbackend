from flask import Blueprint, request, jsonify
from models import Post
from app import db
from utils.decorators import token_required

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

@posts_bp.route('/posts', methods=['POST'])
@token_required
def create_post(current_user):
    data = request.get_json()
    new_post = Post(title=data['title'], description=data['description'], user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'}), 201
