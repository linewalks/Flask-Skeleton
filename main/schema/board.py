from marshmallow import fields, Schema
from main.schema import RequestPagination, ResponsePagination


# Schema
class BoardSchema(Schema):
  title = fields.Str(required=True)
  content = fields.Str(requried=True, allow_none=True)


class BoardInfoSchema(BoardSchema):
  id = fields.Int(required=True)
  created_time = fields.DateTime(required=True)
  updated_time = fields.DateTime(required=True, allow_none=True)
  deleted_time = fields.DateTime(required=True, allow_none=True)


class BoardListSchema(ResponsePagination):
  list = fields.List(
    fields.Nested(BoardInfoSchema), 
    requried=True
  )


# Request
class RequestCreateBoard(BoardSchema):
  pass


class RequestBoardList(RequestPagination):
  pass


class RequestUpdateBoard(BoardSchema):
  pass


# Response
class ResponseBoardList(Schema):
  board_list = fields.Nested(
      BoardListSchema,
      requried=True,
      data_key="boardList"
  )


class ResponseBoardInfo(Schema):
  board_info = fields.Nested(
      BoardInfoSchema,
      requried=True,
      data_key="boardInfo"
  )
