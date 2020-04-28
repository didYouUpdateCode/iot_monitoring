from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.user import User, UserSchema


class Me(Resource):
    @jwt_required
    def get(self):
        user = User.query.filter_by(email=get_jwt_identity()).first()
        if not user:
            return {'message': 'User is not found.'}, 400

        user_schema = UserSchema(exclude=['password'])
        return user_schema.dump(user)
