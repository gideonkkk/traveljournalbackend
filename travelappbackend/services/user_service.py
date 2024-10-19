from travelappbackend.models import User, db

# Get user by ID
def get_user_by_id(user_id):
    return User.query.get(user_id)

# Follow a user
def follow_user(current_user_id, target_user_id):
    current_user = User.query.get(current_user_id)
    target_user = User.query.get(target_user_id)
    
    if not target_user or target_user_id in [u.id for u in current_user.following]:
        return None

    current_user.following.append(target_user)
    db.session.commit()
    return target_user
