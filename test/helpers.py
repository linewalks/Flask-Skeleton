import json
from marshmallow import ValidationError


def to_json(data):
  return json.loads(data)


def _test_get_status_code(client, status_code, url, query_string=None, schema=None):
  rv = client.get(url, query_string=query_string)
  assert rv.status_code == status_code
  if schema:  # validate schema
    errors = schema.validate(rv.json)
    if errors:
      raise ValidationError(errors)
  return rv


def _test_post_status_code(client, status_code, url, json=None, schema=None):
  rv = client.post(url, json=json)
  assert rv.status_code == status_code
  if schema:  # validate schema
    errors = schema.validate(rv.json)
    if errors:
      raise ValidationError(errors)
  return rv


def _test_delete_status_code(client, status_code, url, json=None, schema=None):
  rv = client.delete(url, json=json)
  assert rv.status_code == status_code
  if schema:  # validate schema
    errors = schema.validate(rv.json)
    if errors:
      raise ValidationError(errors)
  return rv


def _test_get_error(client, error, url, query_string=None):
  rv = client.get(url, query_string=query_string)
  assert rv.status_code == error.code

  data = rv.json
  assert data["msgId"] == error.id
  return rv


def _test_post_error(client, error, url, json=None):
  rv = client.post(url, json=json)
  assert rv.status_code == error.code

  data = rv.json
  assert data["msgId"] == error.id
  return rv


def _test_delete_error(client, error, url, json=None):
  rv = client.delete(url, json=json)
  assert rv.status_code == error.code

  data = rv.json
  assert data["msgId"] == error.id
  return rv
