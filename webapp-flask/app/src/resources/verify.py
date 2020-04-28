from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims
from .. import db
from ..models.user import User, UserSchema


class Verify(Resource):
    @jwt_required
    def get(self):
        email = get_jwt_identity()
        pwd_hash = get_jwt_claims().get('pwd_hash')

        if not pwd_hash:
            return {'message': 'Missing hashed password'}, 400
        elif User.query.filter_by(email=email).first():
            return {'message': 'This email is already verified.'}, 400

        user = User(email=email, password=pwd_hash)
        db.session.add(user)
        db.session.commit()

        user_schema = UserSchema(exclude=['password'])
        return {'user': user_schema.dump(user), 'message': 'Account is created'}, 201
