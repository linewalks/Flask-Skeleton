from flask import Blueprint
from flask_apispec import doc, marshal_with, use_kwargs

from main.controllers.common import (
    get_board_list,
    check_board_exisitence
)
from main.models.board import Board
from main.models.comment import Comment
from main.models.common.error import (
    ResponseError,
    ERROR_BOARD_NOT_FOUND,
    SUCCESS_CREATE_BOARD,
    SUCCESS_DELETE_BOARD,
    SUCCESS_PERMANENTLY_DELETE_BOARD,
    SUCCESS_UPDATE_BOARD
)
from main.schema.board import (
    RequestBoardList,
    RequestCreateBoard,
    RequestUpdateBoard,
    ResponseBoardInfo,
    ResponseBoardList
)


API_CATEGORY = "Board"
board_bp = Blueprint("board", __name__, url_prefix="/api/board")


@board_bp.route("/create", methods=["POST"])
@use_kwargs(RequestCreateBoard)
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판을 생성",
    description="게시판을 생성 합니다."
)
def create_board(title, content):
  Board.insert(
      title=title,
      content=content
  )
  return SUCCESS_CREATE_BOARD.get_response()


@board_bp.route("/list", methods=["GET"])
@use_kwargs(RequestBoardList, location="query")
@marshal_with(ResponseBoardList, code=200)
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판 목록 리스트",
    description="게시판 목록 리스트를 불러옵니다."
)
def get_board_info_list(page, length):
  board_list = get_board_list(page, length)
  return {
      "board_list": board_list
  }


@board_bp.route("/<int:board_id>", methods=["GET"])
@marshal_with(ResponseBoardInfo, code=200)
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판 정보",
    description="게시판 정보를 확인합니다."
)
@check_board_exisitence
def get_board_info(board):
  comment_list = Comment.get_list(board.id)
  return {
      "board_info": board.as_dict(),
      "comment_list": comment_list
  }


@board_bp.route("/<int:board_id>", methods=["POST"])
@use_kwargs(RequestUpdateBoard)
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판 수정",
    description="게시판을 수정합니다."
)
@check_board_exisitence
def update_board_info(board, title, content):
  board.update(
      title=title,
      content=content
  )
  return SUCCESS_UPDATE_BOARD.get_response()


@board_bp.route("/<int:board_id>/delete", methods=["POST"])
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판 삭제",
    description="게시판을 식제합니다."
)
@check_board_exisitence
def delete_board_info(board):
  board.soft_delete()
  return SUCCESS_DELETE_BOARD.get_response()


@board_bp.route("/<int:board_id>/delete", methods=["DELETE"])
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="게시판 영구 삭제",
    description="게시판을 영구 식제합니다."
)
def permanently_delete_board_info(board_id):
  board = Board.get(board_id, is_deleted=True)
  if not board:
    return ERROR_BOARD_NOT_FOUND.get_response()
  Board.delete(board)
  return SUCCESS_PERMANENTLY_DELETE_BOARD.get_response()
