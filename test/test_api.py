import pytest

from main.models.common.error import (
    ERROR_BOARD_NOT_FOUND,
    ERROR_COMMENT_NOT_FOUND,
    ResponseError
)
from main.schema.board import (
    ResponseBoardInfo,
    ResponseBoardList
)
from main.schema.comment import ResponseCommentInfo
from test.helpers import (
  _test_get_status_code,
  _test_post_status_code,
  _test_delete_status_code,
  _test_get_error,
  _test_post_error,
  _test_delete_error
)


class TestBoard:
  
  @pytest.fixture(scope="class")
  def board(self, db):
    from main.models.board import Board
    board = Board(
        title="example board",
        content="example content"
    )
    db.session.add(board)
    db.session.commit()
    yield board
    db.session.delete(board)
    db.session.commit()


  def test_create_board(self, client):
    _test_post_status_code(
        client,
        200,
        "/api/board/create",
        {
            "title": "test_board",
            "content": "this board is test board"
        },
        schema=ResponseError()
    )

  def test_get_board_info(self, client, board):
    _test_get_status_code(
        client,
        200,
        f"/api/board/{board.id}",
        schema=ResponseBoardInfo()
    )
  
  def test_get_board_info_not_found(self, client):
    _test_get_error(
        client,
        ERROR_BOARD_NOT_FOUND,
        "/api/board/0"
    )
  
  @pytest.mark.parametrize("page", [1, 5, 10])
  @pytest.mark.parametrize("length", [0, 10, 20])
  def test_get_board_info_list(self, client, page, length):
    _test_get_status_code(
        client,
        200,
        f"/api/board/list",
        {"page": page, "length": length},
        schema=ResponseBoardList()
    )

  def test_update_board(self, client, board):
    _test_post_status_code(
        client,
        200,
        f"/api/board/{board.id}",
        {
            "title": "change example board",
            "content": "change this board is test board"
        },
        schema=ResponseError()
    )
  
  def test_update_board_not_found(self, client):
    _test_post_error(
        client,
        ERROR_BOARD_NOT_FOUND,
        "/api/board/0",
        {
            "title": "change example board",
            "content": "change this board is test board"
        }
    )

  def test_delete_board(self, client, board):
    _test_post_status_code(
        client,
        200,
        f"/api/board/{board.id}/delete",
        schema=ResponseError()
    )
  
  def test_delete_board_not_found(self, client, board):
    _test_post_error(
        client,
        ERROR_BOARD_NOT_FOUND,
        f"/api/board/{board.id}/delete"
    )

  def test_permanently_delete_board(self, client, board):
    _test_delete_status_code(
        client,
        200,
        f"/api/board/{board.id}/delete",
        {
            "title": "change example board",
            "content": "change this board is test board"
        },
        schema=ResponseError()
    )
  
  def test_permanently_delete_board_not_found(self, client, board):
    _test_delete_error(
        client,
        ERROR_BOARD_NOT_FOUND,
        f"/api/board/{board.id}/delete",
        {
            "title": "change example board",
            "content": "change this board is test board"
        }
    )


class TestComment:
  @pytest.fixture(scope="class")
  def board(self, db):
    from main.models.board import Board
    board = Board(
        title="example board",
        content="example content"
    )
    db.session.add(board)
    db.session.commit()
    yield board
    db.session.delete(board)
    db.session.commit()
  
  @pytest.fixture(scope="function")
  def comment(self, db, board):
    from main.models.comment import Comment
    comment = Comment(
        board_id=board.id,
        content="example comment content"
    )
    db.session.add(comment)
    db.session.commit()
    yield comment
    db.session.delete(comment)
    db.session.commit()
  
  def test_create_comment(self, client, board):
    _test_post_status_code(
        client,
        200,
        f"/api/comment/{board.id}/create",
        {"content": "test comment"}
    )

  def test_get_comment_info(self, client, board, comment):
    _test_get_status_code(
        client,
        200,
        f"/api/comment/{board.id}/{comment.id}",
        schema=ResponseCommentInfo()
    )
  
  def test_get_comment_info_not_found(self, client, board):
    _test_get_error(
        client,
        ERROR_COMMENT_NOT_FOUND,
        f"/api/comment/{board.id}/0"
    )
  
  def test_upgrade_comment(self, client, board, comment):
    _test_post_status_code(
        client,
        200,
        f"/api/comment/{board.id}/{comment.id}",
        {"content": "change example comment"}
    )
  
  def test_upgrade_comment_not_found(self, client, board):
    _test_post_error(
        client,
        ERROR_COMMENT_NOT_FOUND,
        f"/api/comment/{board.id}/0",
        {"content": "not found"}
    )
  
  def test_delete_comment(self, client, board, comment):
    _test_delete_status_code(
        client,
        200,
        f"/api/comment/{board.id}/{comment.id}"
    )

  def test_delete_comment_not_found(self, client, board):
    _test_delete_error(
        client,
        ERROR_COMMENT_NOT_FOUND,
        f"/api/comment/{board.id}/0"
    )
