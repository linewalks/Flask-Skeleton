from main import db


class BaseTable(db.Model):
  __abstract__ = True

  @staticmethod
  def delete(obj, commit=True):
    db.session.delete(obj)
    if commit:
      db.session.commit()
