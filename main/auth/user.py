from flask_apispec import use_kwargs, marshal_with, doc
from . import auth_bp, API_CATEGORY
from .common.skeleton import check_test_id_exists
from .. import app, db
from ..models.resources import RequestBodySchema, RequestParameterSchema, ResponseBodySchema
from ..models.user import User
from ..models.common.error import (
    ResponseError,
    ERROR_ID_NOT_EXISTS,
    ERROR_ID_ALREADY_EXISTS,
    ERROR_PARAMETER_NOT_EXISTS,
    ERROR_BODY_NOT_EXISTS,
    SUCCESS_ID_DELETE,
    SUCCESS_ID_UPDATE,
    SUCCESS_ID_INSERT
)


@auth_bp.route('/signin', methods=['POST'])
@use_kwargs(RequestParameterSchema, locations=("querystring"))
@marshal_with(ResponseBodySchema, code=200)
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="로그인",
     description="사용자 로그인을 합니다")
def signin(**kwargs):
  pass
