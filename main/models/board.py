from sqlalchemy import func

from main import db
from main.models import schema
from main.models.common.base import BaseTable


class Board(BaseTable):
  __tablename__ = "board"
  __table_args__ = {"schema": schema, "extend_existing": True}
  id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
  title = db.Column(db.String(50), nullable=False) 
  content = db.Column(db.String(1024))
  created_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
  updated_time = db.Column(db.DateTime)
  # 삭제 되지 않은 프로젝트 검색시 쿼리 성능 향상을 위한 index
  deleted_time = db.Column(db.DateTime, index=True)

  @classmethod
  def get(cls, board_id):
    board = cls.query.filter(
        cls.id==board_id,
        cls.deleted_time.is_(None)
    ).one_or_none()
    return board
  
  @classmethod
  def get_deleted_board(cls, board_id):
    board = cls.query.filter(
        cls.id==board_id,
        cls.deleted_time.isnot(None)
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
