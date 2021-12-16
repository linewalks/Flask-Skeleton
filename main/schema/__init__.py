from marshmallow import fields, Schema, validate


class RequestPagination(Schema):
  page = fields.Int(
      missing=1,
      validate=validate.Range(min=1)
  )
  length = fields.Int(
      missing=0,
      validate=validate.Range(min=0)
  )


class ResponsePagination(Schema):
  page = fields.Int(validate=validate.Range(min=1))
  total_length = fields.Int(data_key="totalLength")
