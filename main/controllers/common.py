from functools import wraps

from main.models.board import Board
from main.models.common.error import ERROR_BOARD_NOT_FOUND


def get_page_offset(page, length):
  return length * (page - 1)


def get_board_list(page, length):
  page_offset = get_page_offset(page, length)
  query = Board.query.filter(
      Board.deleted_time.is_(None)
  ).order_by(Board.id)

  total_length = query.count()

  if length != 0:
    query = query.offset(page_offset).limit(length)

  boards = query.all()
  board_list = [
      board.as_dict()
      for board in boards
  ]

  return {
      "page": page,
      "list": board_list,
      "total_length": total_length
  }


def check_board_exisitence(fn):  

  @wraps(fn)
  def wrapper(*args, **kwargs):
    if "board_id" not in kwargs:
        raise Exception("check_board_exisitence must used with board_id")
    board_id = kwargs["board_id"]
    board = Board.get(board_id)
    if not board:
      return ERROR_BOARD_NOT_FOUND.get_response()

    kwargs["board"] = board
    del kwargs["board_id"]

    return fn(*args, **kwargs)

  return wrapper
