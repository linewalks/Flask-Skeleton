from flask import current_app as app
from sqlalchemy import func

from main import db
from main.models.common.base import BaseTable


schema = app.config["SCHEMA_TEST"]


class Board(BaseTable):
  __tablename__ = "board"
  __table_args__ = {"schema": schema, "extend_existing": True}
  id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
  title = db.Column(db.String(50), nullable=False) 
  content = db.Column(db.String(1024))
  created_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
  updated_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
  # 삭제 되지 않은 프로젝트 검색시 쿼리 성능 향상을 위한 index
  deleted_time = db.Column(db.DateTime, index=True)

  @classmethod
  def get(cls, board_id, is_deleted=False):
    if is_deleted:
      delete_conditon = cls.deleted_time.isnot(None)
    else:
      delete_conditon = cls.deleted_time.is_(None)
    board = cls.query.filter(
        cls.id == board_id,
        delete_conditon
    ).one_or_none()
    return board

  def update(self, title, content):
    self.title = title
    self.content = content
    self.updated_time = func.now()
    db.session.commit()

  def soft_delete(self):
    self.deleted_time = func.now()
    db.session.commit()
