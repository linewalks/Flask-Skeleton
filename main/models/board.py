from sqlalchemy import func

from main import db
from main.models import schema
from main.models.common.base import BaseTable


class Board(BaseTable, db.Model):
  __table_name__ = "board"
  __table_args__ = {"schema": schema, "extend_existing": True}
  id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
  title = db.Column(db.String(50), nullable=False) 
  content = db.Column(db.String(1024))
  created_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
  updated_time = db.Column(db.DateTime)
  # 삭제 되지 않은 프로젝트 검색시 쿼리 성능 향상을 위한 index
  deleted_time = db.Column(db.DateTime, index=True)
