from marshmallow import fields, Schema


class Error:
  def __init__(self, id, msg, code):
    self.id = id
    self.msg = msg
    self.code = code

  def get_response(self, **msg_kwargs):
    msg = self.msg.format(**msg_kwargs)
    return {"msg_id": self.id, "msg": msg}, self.code


class ResponseError(Schema):
  msg_id = fields.Str(data_key="msgId")
  msg = fields.Str()


# 에러 코드 정의 방법
# 같은 카테고리의 에러는 뒤 숫자만 변경 u001, u002, u003
# 새로운 카테고리의 에러는 앞 숫자 변경 u101, u201
# 같은 에러지만 상태 코드가 다른 경우, 같은 에러 코드를 쓴다
# 성공이지만 메세지가 필요한 경우, 다음과 같이 명명한다. SUCCESS_*
ERROR_BOARD_NOT_FOUND = Error("u001", "Board not found.", 404)
SUCCESS_CREATE_BOARD = Error("u011", "Success to register the board.", 200)
SUCCESS_UPDATE_BOARD = Error("u012", "Success to update the board.", 200)
SUCCESS_DELETE_BOARD = Error("u013", "Success to delete the board.", 200)
SUCCESS_PERMANENTLY_DELETE_BOARD = Error("u014", "Success to permanently delete the board.", 200)

ERROR_COMMENT_NOT_FOUND = Error("u101", "Comment not found.", 404)
SUCCESS_CREATE_COMMENT = Error("u111", "Success to register the comment.", 200)
SUCCESS_UPDATE_COMMENT = Error("u112", "Success to update the comment.", 200)
SUCCESS_DELETE_COMMENT = Error("u113", "Success to delete the comment.", 200)
