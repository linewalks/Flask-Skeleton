from marshmallow import fields, Schema


# Requests
class RequestBodySchema(Schema):
  id = fields.Int(required=True)
  name = fields.Str(required=True)
  count = fields.Int(required=True)


class RequestParameterSchema(Schema):
  id = fields.Int(required=True, location='query')


class RequestLoginSchema(Schema):
  email = fields.Str(required=True)
  password = fields.Str(required=True)


class RequestEmailVerification(Schema):
  email = fields.Str()
  token = fields.Str()


# Response
class ResponseBodySchema(Schema):
  skeleton = fields.Nested(RequestBodySchema)


class ResponseLoginSchema(Schema):
  access_token = fields.Str()
  refresh_token = fields.Str()
  email = fields.Str()


class ResponseAccessTokenSchema(Schema):
  access_token = fields.Str()
