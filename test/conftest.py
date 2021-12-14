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
def client(app):
  client = app.test_client()
  yield client
