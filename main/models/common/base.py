from main import db


class BaseTable(db.Model):
  __abstract__ = True

  def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}

  @classmethod
  def insert(cls, **kwargs):
    obj = cls(**kwargs)
    db.session.add(obj)
    db.session.commit()

  @staticmethod
  def delete(obj):
    db.session.delete(obj)
    db.session.commit()
