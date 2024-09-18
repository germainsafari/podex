from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    from app.routes import auth, pokemon
    app.register_blueprint(auth.bp)
    app.register_blueprint(pokemon.bp)

    return app
