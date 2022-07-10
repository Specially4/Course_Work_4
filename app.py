from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.user import users_ns
from views.auth import auth_ns
from views.director import directors_ns
from views.genre import genres_ns
from views.movie import movies_ns

app = Flask(__name__)
app_config = Config()
app.config.from_object(app_config)
app.app_context().push()

db.init_app(app)
api = Api(app)
api.add_namespace(directors_ns)
api.add_namespace(genres_ns)
api.add_namespace(movies_ns)
api.add_namespace(users_ns)
api.add_namespace(auth_ns)

if __name__ == '__main__':
    app.run()
