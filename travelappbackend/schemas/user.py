from marshmallow import Schema, fields
from travelappbackend.models import User

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    followers_count = fields.Method("get_followers_count")
    following_count = fields.Method("get_following_count")

    def get_followers_count(self, obj):
        return len(obj.followers)

    def get_following_count(self, obj):
        return len(obj.following)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
