from main.models.board import Board


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