from flask import Blueprint
from flask_apispec import doc, marshal_with, use_kwargs

from main.controllers.common import check_board_exisitence
from main.models.comment import Comment
from main.models.common.error import (
    ERROR_COMMENT_NOT_FOUND,
    ResponseError,
    SUCCESS_CREATE_COMMENT,
    SUCCESS_DELETE_COMMENT,
    SUCCESS_UPDATE_COMMENT
)
from main.schema.comment import (
    RequestCreateComment,
    RequestUpdateComment,
    ResponseCommentInfo
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


@comment_bp.route("/<int:board_id>/<int:comment_id>", methods=["GET"])
@marshal_with(ResponseCommentInfo, code=200)
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판 댓글 정보",
    description="해당 게시판의 댓글을 정보를 확인 합니다."
)
@check_board_exisitence
def get_comment_info(board, comment_id):
  comment = Comment.get(
      comment_id,
      board.id
  )
  if not comment:
    return ERROR_COMMENT_NOT_FOUND.get_response()

  return {
      "comment_info": comment.as_dict()
  }


@comment_bp.route("/<int:board_id>/<int:comment_id>", methods=["POST"])
@use_kwargs(RequestUpdateComment)
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판 댓글 수정",
    description="해당 게시판의 댓글을 수정 합니다."
)
@check_board_exisitence
def update_comment(board, comment_id, content):
  comment = Comment.get(
      comment_id,
      board.id
  )
  if not comment:
    return ERROR_COMMENT_NOT_FOUND.get_response()
  comment.update(content)
  return SUCCESS_UPDATE_COMMENT.get_response()


@comment_bp.route("/<int:board_id>/<int:comment_id>", methods=["DELETE"])
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판 댓글 삭제",
    description="해당 게시판의 댓글을 삭제 합니다."
)
@check_board_exisitence
def delete_comment(board, comment_id):
  comment = Comment.get(
      comment_id,
      board.id
  )
  if not comment:
    return ERROR_COMMENT_NOT_FOUND.get_response()
  Comment.delete(comment)
  return SUCCESS_DELETE_COMMENT.get_response()
