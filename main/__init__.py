import configparser
import os
import decimal
import flask.json
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy import MetaData, create_engine
from flask_sqlalchemy import SQLAlchemy
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask_apispec.extension import FlaskApiSpec

app = Flask(__name__)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='skeleton',
        version='v1',
        openapi_version="2.0.0",
        plugins=[MarshmallowPlugin()],

    ),
    'APISPEC_SWAGGER_URL': '/docs.json',
    'APISPEC_SWAGGER_UI_URL': '/docs/'
})
docs = FlaskApiSpec(app)


CORS(app)
api = Api(app)


# Blueprint
from .controllers import skeleton_bp
blueprints = [
    skeleton_bp
]

for bp in blueprints:
  app.register_blueprint(bp)
docs.register_existing_resources()

# 스웨거에서 options 제거
for key, value in docs.spec._paths.items():
  docs.spec._paths[key] = {
      inner_key: inner_value for inner_key, inner_value in value.items() if inner_key != "options"
  }
