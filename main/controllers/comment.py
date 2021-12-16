from flask import Blueprint
from flask_apispec import doc, marshal_with, use_kwargs

from main.controllers.common import check_board_exisitence
from main.models.board import Board
from main.models.comment import Comment
from main.models.common.error import (
    ResponseError,
    SUCCESS_CREATE_COMMENT
)
from main.schema.comment import (
    RequestCreateComment
)


API_CATEGORY = "Comment"
comment_bp = Blueprint("comment", __name__, url_prefix="/api/comment")


@comment_bp.route("/<int:board_id>/create", methods=["POST"])
@use_kwargs(RequestCreateComment)
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판을 생성",
    description="게시판을 생성 합니다."
)
@check_board_exisitence
def create_board(board, content):
  Comment.insert(
      board_id=board.id,
      content=content
  )
  return SUCCESS_CREATE_COMMENT.get_response()
