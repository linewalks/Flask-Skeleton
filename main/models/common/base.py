from main import db


class BaseTable(db.Model):
  __abstract__ = True

  def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

  def as_clear_dict(self):
    _dict = {}
    for c in self.__table__.columns:
      if c.foreign_keys:
        continue
      val = getattr(self, c.name)
      if val:
        _dict[c.name] = val
    return _dict

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
