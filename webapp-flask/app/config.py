import os

# app
EMAIL_VERIFICATION = os.getenv('EMAIL_VERIFICATION', False)

# flask
PROPAGATE_EXCEPTIONS = True

# flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@postgres:5432/postgres'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# flask-jwt-extended
JWT_ERROR_MESSAGE_KEY = 'message'
JWT_TOKEN_LOCATION = ['query_string', 'headers']
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret')

# flask-mail
MAIL_SERVER = os.getenv('MAIL_SERVER', 'localhost')
MAIL_PORT = os.getenv('MAIL_PORT', 25)
MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', False)
MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', False)
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
