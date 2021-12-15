from flask import Blueprint
from flask_apispec import doc, marshal_with, use_kwargs

from main import db
from main.controllers.common import get_board_list
from main.models.board import Board
from main.models.common.error import (
    ResponseError,
    SUCCESS_CREATE_BOARD
)
from main.schema.board import (
    RequestCreateBoard,
    RequestBoardList,
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