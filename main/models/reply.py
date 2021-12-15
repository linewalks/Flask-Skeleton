from flask import current_app as app
from sqlalchemy import func, case
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql.expression import update

from main import db
from main.models.board import Board
from main.models.common.base import BaseTable


schema = app.config["SCHEMA_TEST"]


class Reply(BaseTable):
  __tablename__ = "reply"
  __table_args__ = {"schema": schema, "extend_existing": True}
  # ondelete="CASCADE"를 지정하여 Board가 삭제시 자동적으로 해당된 댓글 또한 삭제
  id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
  board_id = db.Column(db.Integer, db.ForeignKey(Board.id, ondelete="CASCADE"), nullable=True)
  comment = db.Column(db.String(256))
  created_time = db.Column(db.DateTime, nullable=False, server_default=func.now())
  updated_time = db.Column(db.DateTime, nullable=False, server_default=func.now())

  @hybrid_property
  def recent_time(self):
    return  case(
        [(self.updated_time > self.created_time, self.updated_time),],
        else_ = self.created_time
    )

  @classmethod
  def get_list(cls, board_id):
    replies = cls.query.filter(
        cls.board_id==board_id
    ).order_by(
        cls.recent_time.desc()
    )
    replies = replies.all()
    reply_list = [
      reply.as_dict()
      for reply in replies
    ]
    return reply_list
