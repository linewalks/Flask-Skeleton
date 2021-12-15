from marshmallow import fields, Schema, validate
from main.schema import RequestPagination, ResponsePagination


# Schema
class BoardSchema(Schema):
  title = fields.Str(required=True)
  content = fields.Str(requried=True, allow_none=True)


class BoardInfoSchema(BoardSchema):
  id = fields.Int(required=True)
  created_time = fields.DateTime(required=True)
  updated_time = fields.DateTime(required=True)
  deleted_time = fields.DateTime(required=True, allow_none=True)


class BoardListSchmea(ResponsePagination):
  list = fields.List(
    fields.Nested(BoardInfoSchema), 
    requried=True
  )


# Request
class RequestCreateBoard(BoardSchema):
  pass


class RequestBoardList(RequestPagination):
  pass


# Response
class ResponseBoardList(Schema):
  board_list = fields.Nested(
      BoardListSchmea,
      requried=True,
      data_key="boardList"
  )


class ResponseBoardInfo(Schema):
  board_info = fields.Nested(
      BoardInfoSchema,
      requried=True,
      data_key="boardInfo"
  )