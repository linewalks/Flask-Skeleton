from flask import Blueprint
from flask_apispec import doc, marshal_with, use_kwargs

from main.controllers.common import check_board_exisitence
from main.models.board import Board
from main.models.comment import Comment
from main.models.common.error import (
    ERROR_COMMENT_DOES_NOT_EXISTS,
    ResponseError,
    SUCCESS_CREATE_COMMENT,
    SUCCESS_UPDATE_COMMENT
)
from main.schema.comment import (
    RequestCreateComment,
    RequestUpdateComment
)


API_CATEGORY = "Comment"
comment_bp = Blueprint("comment", __name__, url_prefix="/api/comment")


@comment_bp.route("/<int:board_id>/create", methods=["POST"])
@use_kwargs(RequestCreateComment)
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판 댓글 생성",
    description="해당 게시판의 댓글을 생성 합니다."
)
@check_board_exisitence
def create_comment(board, content):
  Comment.insert(
      board_id=board.id,
      content=content
  )
  return SUCCESS_CREATE_COMMENT.get_response()


@comment_bp.route("/<int:board_id>/update", methods=["POST"])
@use_kwargs(RequestUpdateComment)
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판 댓글 생성",
    description="해당 게시판의 댓글을 생성 합니다."
)
@check_board_exisitence
def update_comment(board, comment_id, content):
  comment = Comment.get(
      comment_id,
      board.id
  )
  if not comment:
    return ERROR_COMMENT_DOES_NOT_EXISTS.get_response()
  comment.update(content)
  return SUCCESS_UPDATE_COMMENT.get_response()
