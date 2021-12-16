from marshmallow import fields, Schema


# Schema
class CommentSchema(Schema):
  content = fields.Str(requried=True)


# Request
class RequestCreateComment(CommentSchema):
  pass


# Response
