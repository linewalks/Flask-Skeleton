from flask import Blueprint
from flask_apispec import doc, marshal_with, use_kwargs

from main import db
from main.models.board import Board
from main.models.common.error import (
    ResponseError,
    SUCCESS_CREATE_BOARD
)
from main.schema.board import RequestCreateBoard


API_CATEGORY = "Board"
board_bp = Blueprint("board", __name__, url_prefix="/api")


@board_bp.route("/create", methods=["POST"])
@use_kwargs(RequestCreateBoard)
@marshal_with(ResponseError)
@doc(
    tags=[API_CATEGORY],
    summary="create board",
    description="create board"
)
def create_board(title, content):
  Board.insert(
      title=title,
      content=content
  )
  return SUCCESS_CREATE_BOARD.get_response()
