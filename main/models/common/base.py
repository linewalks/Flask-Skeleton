from main import db


class BaseTable:
  @staticmethod
  def delete(obj, commit=True):
    db.session.delete(obj)
    if commit:
      db.session.commit()