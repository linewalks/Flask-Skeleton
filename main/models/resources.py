from marshmallow import fields, Schema


# Requests
class RequestBodySchema(Schema):
  id = fields.Int(required=True)
  name = fields.Str(required=True)
  count = fields.Int(required=True)


class RequestParameterSchema(Schema):
  id = fields.Int(required=True, location='query')


# Response
class ResponseBodySchema(Schema):
  skeleton = fields.Nested(RequestBodySchema)
