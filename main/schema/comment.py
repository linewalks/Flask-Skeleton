from marshmallow import fields, Schema


# Schema
class CommentContentSchema(Schema):
  content = fields.Str(requried=True)


class CommentSchema(CommentContentSchema):
  id = fields.Int(required=True)
  board_id = fields.Int(required=True, data_key="boardId")
  created_time = fields.DateTime(required=True, data_key="createdTime")
  updated_time = fields.DateTime(required=True, allow_none=True, data_key="updatedTime")


# Request
class RequestCreateComment(CommentContentSchema):
  pass


class RequestUpdateComment(CommentContentSchema):
  pass


# Response
class ResponseCommentInfo(Schema):
  comment_info = fields.Nested(
      CommentSchema,
      required=True,
      data_key="commentInfo"
  )
