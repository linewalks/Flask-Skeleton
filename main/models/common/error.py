from marshmallow import fields, Schema


class Error:
  def __init__(self, id, msg, code):
    self.id = id
    self.msg = msg
    self.code = code

  def get_response(self, **msg_kwargs):
    msg = self.msg.format(**msg_kwargs)
    return {'msg_id': self.id, 'msg': msg}, self.code


class ResponseError(Schema):
  msgId = fields.Str(attribute='msg_id')
  msg = fields.Str()


# 에러 코드 정의 방법
# 같은 카테고리의 에러는 뒤 숫자만 변경 u001, u002, u003
# 새로운 카테고리의 에러는 앞 숫자 변경 u101, u201
# 같은 에러지만 상태 코드가 다른 경우, 같은 에러 코드를 쓴다
# 성공이지만 메세지가 필요한 경우, 다음과 같이 명명한다. SUCCESS_*
ERROR_ID_NOT_EXISTS = Error('u101', "Id not exists.", 400)
ERROR_ID_ALREADY_EXISTS = Error('u102', "Id already exists.", 400)

SUCCESS_ID_INSERT = Error('u202', "id insert success.", 200)
SUCCESS_ID_UPDATE = Error('u203', "id update success.", 200)
SUCCESS_ID_DELETE = Error('u204', "id delete success.", 200)

ERROR_PARAMETER_NOT_EXISTS = Error('u301', "parameter not exists.", 400)
ERROR_BODY_NOT_EXISTS = Error('u302', "body not exists.", 400)
