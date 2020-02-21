from ... import app, db
from ...models.data import t_test_log

schema_name = app.config['SCHEMA_TEST']


def get_test_id_info(test_id):
  return db.session.query(t_test_log).filter(t_test_log.c.id == test_id).first()


def check_test_id_exists(test_id):
  return get_test_id_info(test_id) is not None
