import pytest

import json
from . import to_json
from main import db
from flask import g
from main.models.data import t_test_log


@pytest.fixture(scope="function")
def session():
    session = db.session
    g.db = session
    yield session
    session.rollback()
    session.close()


@pytest.mark.parametrize("id", [1, 5, 10, 100])
@pytest.fixture(scope="function")
def user(session, id):
    session.execute(
        t_test_log.delete().where(
            t_test_log.c.id == id
        )
    )


# 공통 함수
def simple_get_test_status_code(client, status_code, url, query_string=None):
  rv = client.get(url, query_string=query_string)
  assert rv.status_code == status_code
  return rv


def simple_post_test_status_code(client, status_code, url, body=None):
    mimetype = "application/json"
    headers = {
        "Content-Type": mimetype,
        "Accept": mimetype
    }
    rv = client.post(url, data=json.dumps(body), headers=headers)
    response = to_json(rv.data)
    assert rv.content_type == mimetype
    assert rv.status_code == status_code
    return rv


def simple_get_test_status_code_200(client, url, query_string=None):
  return simple_get_test_status_code(client, 200, url, query_string)


def simple_get_test_status_code_404(client, url, query_string=None):
  return simple_get_test_status_code(client, 404, url, query_string)


def simple_post_test_status_code_200(client, url, body=None):
  return simple_post_test_status_code(client, 200, url, body)


@pytest.fixture(scope="class", autouse=True)
def client(app):
  client = app.test_client()
  yield client


class TestSkeleton():
  @pytest.mark.parametrize("id", [1])
  def test_get_skeleton_success(self, client, id):
    simple_get_test_status_code_200(client, "/api/skeleton", f"id={id}")

  def test_get_skeleton_not_found(self, client):
    simple_get_test_status_code_404(client, "/api/skeleton")

  @pytest.mark.parametrize("id", [1, 5, 10, 100])
  def test_post_skeleton_success(self, client, user, id):
      data = {"id": id, "name": "test_name", "count": 10}
      simple_post_test_status_code_200(client, "/api/skeleton", data)
