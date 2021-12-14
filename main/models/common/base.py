from main import db


class BaseTable(db.Model):
  __abstract__ = True

  @classmethod
  def insert(cls, **kwargs):
    obj = cls(**kwargs)
    db.session.add(obj)
    db.session.commit()

  @staticmethod
  def delete(obj, commit=True):
    db.session.delete(obj)
    if commit:
      db.session.commit()
