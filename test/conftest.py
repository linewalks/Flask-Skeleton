import pytest


from main import app as main_app


@pytest.fixture(scope="class")
def app():
  app_context = main_app.app_context()
  app_context.push()

  yield main_app

  app_context.pop()


@pytest.fixture(scope="class", autouse=True)
def client(app):
  client = app.test_client()
  yield client
