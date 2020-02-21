from sqlalchemy import BigInteger, Column, Integer, String, Table
from .. import app, db


t_test_log = db.Table(
    'test',
    db.Column('id', db.BigInteger, primary_key=True),
    db.Column('name', db.String),
    db.Column('count', db.BigInteger),

    schema=app.config['SCHEMA_TEST'],
    extend_existing=True
)


def get_test_id_in_table(test_id):
  count_row = db.session.query(t_test_log).filter(t_test_log.c.id == test_id).first()
  return count_row._asdict()


def insert_test_id_in_table(test_id, test_name, test_count):
  db.session.execute(
      t_test_log.insert().values({
          t_test_log.c.id: test_id,
          t_test_log.c.name: test_name,
          t_test_log.c.count: test_count
      })
  )
  db.session.commit()


def update_test_id_in_table(test_id, test_name, test_count):
  db.session.query(t_test_log).filter(t_test_log.c.id == test_id)\
            .update({t_test_log.c.name: test_name,
                     t_test_log.c.count: test_count},
                    synchronize_session=False)
  db.session.commit()


def delete_test_id_in_table(test_id):
  db.session.query(t_test_log).filter(t_test_log.c.id == test_id).delete()
  db.session.commit()
