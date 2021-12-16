from marshmallow import fields, Schema


# Schema
class CommentSchema(Schema):
  content = fields.Str(requried=True)


# Request
class RequestCreateComment(CommentSchema):
  pass


class RequestUpdateComment(CommentSchema):
  comment_id = fields.Int(reqiroed=True)


class RequestDeleteComment(Schema):
  comment_id = fields.Int(reqiroed=True)


# Response
