import configparser
import os
import decimal
import flask.json

from datetime import timedelta
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_compress import Compress
from flask_jwt_extended import JWTManager
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask_apispec.extension import FlaskApiSpec
from main.models.smtp import Smtp


file_path = f"{os.getcwd()}/main/skeleton.cfg"

docs = FlaskApiSpec()
db = SQLAlchemy()
compress = Compress()
jwt = JWTManager()
cors = CORS()
email_sender = Smtp("smtp.gmail.com", 587)

def create_app(file_paht=file_path):
  app = Flask(__name__)

  app.config.from_pyfile(file_path)
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.config.update({
      "APISPEC_SPEC": APISpec(
          title="skeleton",
          version="0.0.1",
          openapi_version="2.0.0",
          plugins=[FlaskPlugin(), MarshmallowPlugin()],

      ),
      "APISPEC_SWAGGER_URL": "/docs.json",
      "APISPEC_SWAGGER_UI_URL": "/docs/"
  })
  app.config["JWT_IDENTITY_CLAIM"] = "identity"
  app.config["JWT_BLACKLIST_ENABLED"] = True
  app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]
  app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=app.config["JWT_ACCESS_TOKEN_EXPIRES_TIME"])
  app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours=app.config["JWT_REFRESH_TOKEN_EXPIRES_TIME"])
  docs.init_app(app)
  db.init_app(app)
  compress.init_app(app)
  jwt.init_app(app)
  cors.init_app(app)
  email_sender.set_account(app.config["EMAIL_ACCOUNT"], app.config["EMAIL_PASSWORD"])

  with app.app_context():
    # Blueprint
    from .controllers import skeleton_bp
    from .controllers.auth import auth_bp
    blueprints = [
        skeleton_bp,
        auth_bp
    ]

    for bp in blueprints:
      app.register_blueprint(bp)
    docs.register_existing_resources()

    # 스웨거에서 options 제거
    for key, value in docs.spec._paths.items():
      docs.spec._paths[key] = {
          inner_key: inner_value for inner_key, inner_value in value.items() if inner_key != "options"
      }

  return app
