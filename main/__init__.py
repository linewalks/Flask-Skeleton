from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask_apispec.extension import FlaskApiSpec


docs = FlaskApiSpec()
cors = CORS()
api = Api()


def create_app():
  app = Flask(__name__)
  app.config.update({
      "APISPEC_SPEC": APISpec(
          title="SKELETON PROJECT API",
          version="2.0.0",
          openapi_version="2.0",
          plugins=[FlaskPlugin(), MarshmallowPlugin()]
      ),
      "APISPEC_SWAGGER_URL": "/docs.json",
      "APISPEC_SWAGGER_UI_URL": "/docs/"
  })

  docs.init_app(app)
  cors.init_app(app)
  api.init_app(app)

  with app.app_context():
    # migration model import

    # Blueprint

    blueprints = [
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
