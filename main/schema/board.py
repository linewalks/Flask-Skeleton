from marshmallow import fields, Schema, validate
from main.schema import RequestPagination, ResponsePagination


# Schema
class BoardSchema(Schema):
  title = fields.Str(required=True)
  content = fields.Str(requried=True, allow_none=True)


# Request
class RequestCreateBoard(BoardSchema):
  pass


# Response
