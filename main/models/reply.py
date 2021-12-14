from sqlalchemy import func

from main import db
from main.models import schema
from main.models.board import Board
from main.models.common.base import BaseTable


class Reply(BaseTable):
  __tablename__ = "reply"
  __table_args__ = {"schema": schema, "extend_existing": True}
  # ondelete="CASCADE"를 지정하여 Board가 삭제시 자동적으로 해당된 댓글 또한 삭제
  id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
  board_id = db.Column(db.Integer, db.ForeignKey(Board.id, ondelete="CASCADE"), nullable=True)
  comment = db.Column(db.String(256))
  created_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
  updated_time = db.Column(db.DateTime)
