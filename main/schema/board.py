from marshmallow import fields, Schema
from main.schema import RequestPagination, ResponsePagination


# Schema
class BoardSchema(Schema):
  title = fields.Str(required=True)
  content = fields.Str(requried=True, allow_none=True)


class BoardCommentSchema(Schema):
  id = fields.Int(required=True)
  board_id = fields.Int(required=True, data_key="boardId")
  comment = fields.Str(requried=True)
  created_time = fields.DateTime(required=True, data_key="createdTime")
  updated_time = fields.DateTime(required=True, allow_none=True, data_key="updatedTime")


class BoardInfoSchema(BoardSchema):
  id = fields.Int(required=True)
  created_time = fields.DateTime(required=True, data_key="createdTime")
  updated_time = fields.DateTime(required=True, allow_none=True, data_key="updatedTime")
  deleted_time = fields.DateTime(required=True, allow_none=True, data_key="deletedTime")


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
  comment_list = fields.List(
      fields.Nested(BoardCommentSchema),
      requried=True,
      data_key="commentList"
  )
