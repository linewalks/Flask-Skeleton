import pytest


@pytest.fixture(scope="session")
def app():
  from main import create_app
  return create_app()


@pytest.fixture(scope="session", autouse=True)
def app_context(app):
  with app.app_context():
    yield app


@pytest.fixture(scope="class", autouse=True)
def client(app_context):
  client = app_context.test_client()
  return client


@pytest.fixture(scope="module")
def db(app_context):
  from main import db
  db.init_app(app_context)
  yield db
