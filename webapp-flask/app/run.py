from src import app, db, api
from src.models.user import User
from src.resources.register import Register
from src.resources.verify import Verify
from src.resources.login import Login
from src.resources.refresh import Refresh
from src.resources.me import Me

with app.app_context():
    db.drop_all()
    db.create_all()

    api.add_resource(Register, "/user/register")
    api.add_resource(Verify, "/user/verify")
    api.add_resource(Login, "/user/login")
    api.add_resource(Refresh, "/user/refresh")
    api.add_resource(Me, "/user/me")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
