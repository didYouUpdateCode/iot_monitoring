from flask import request
from flask_restful import Resource
from flask_marshmallow import exceptions
from flask_jwt_extended import create_access_token, create_refresh_token
from .. import bcrypt, db
from ..models.user import User, UserSchema


class Login(Resource):
    def post(self):
        try:
            # verify format
            data = UserSchema().load(request.json)

            # verify user's email and password
            user = User.query.filter_by(email=data['email']).first()
            if not user:
                return {'message': 'User is not found.'}, 401
            elif not bcrypt.check_password_hash(user.password, data['password']):
                return {'message': 'Password is incorrect'}, 401

            # create JWTs
            access_token = create_access_token(user.email)
            refresh_token = create_refresh_token(user.email)

            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }

        except exceptions.MarshmallowError as error:
            return {'message': error.messages}, 400

        except exceptions.ValidationError as error:
            return {'message': error.messages}, 400
