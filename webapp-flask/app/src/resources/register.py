from datetime import timedelta
from threading import Thread
from flask import request
from flask_restful import Resource
from flask_marshmallow import exceptions
from flask_jwt_extended import create_access_token
from flask_mail import Message
from .. import app, bcrypt, db, api, mail
from ..models.user import User, UserSchema
from ..resources.verify import Verify


class Register(Resource):
    def post(self):
        try:
            # verify format
            data = UserSchema().load(request.json)

            # check duplication
            email = data['email']
            if User.query.filter_by(email=email).first() != None:
                return {'message': 'This email is already used.'}, 400

            # hash password
            pwd = data['password']
            pwd_hash = bcrypt.generate_password_hash(pwd).decode('utf-8')

            if not app.config.get('EMAIL_VERIFICATION'):
                # save to database
                user = User(email=email, password=pwd_hash)
                db.session.add(user)
                db.session.commit()
                return {'email': email, 'message': 'Account is created'}, 201

            # send activation mail
            jwt = create_access_token(email,
                                      expires_delta=timedelta(minutes=10),
                                      user_claims={'pwd_hash': pwd_hash})

            url = f'http://{request.host + api.url_for(Verify)}?jwt={jwt}'
            self.send_activation_mail([email], activation_url=url)

            return {'message': f'A verification link has been sent to {email}.'}

        except exceptions.MarshmallowError as error:
            return {'message': error.messages}, 400

        except exceptions.ValidationError as error:
            return {'message': error.messages}, 400

    def send_activation_mail(self, recipients, activation_url):
        subject = 'Welcome to SSD Control Center'
        mail_body = '\n'.join(['Hello,',
                               'Please click the link below to active your account.',
                               activation_url])

        def _send_activation_mail():
            with app.app_context():
                message = Message(subject='Welcome to SSD Control Center',
                                  recipients=recipients,
                                  body=mail_body)
                mail.send(message)

        thread = Thread(target=_send_activation_mail)
        thread.start()
