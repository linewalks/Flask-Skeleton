from flask import current_app as app
from flask_apispec import use_kwargs, marshal_with, doc
from main.controllers import skeleton_bp, API_CATEGORY
from .common.skeleton import check_test_id_exists
from main import db
from main.models.resources import RequestBodySchema, RequestParameterSchema, ResponseBodySchema
from main.models.data import (
    get_test_id_in_table,
    insert_test_id_in_table,
    update_test_id_in_table,
    delete_test_id_in_table
)
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


@skeleton_bp.route('/skeleton', methods=['GET'])
@use_kwargs(RequestParameterSchema, locations=("querystring"))
@marshal_with(ResponseBodySchema, code=200)
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="skeleton get",
     description="skeleton get")
def skeleton_get(**kwargs):
  test_id = kwargs.get('id', None)
  if test_id is None:
    return ERROR_PARAMETER_NOT_EXISTS.get_response()
  if not check_test_id_exists(test_id):
    return ERROR_ID_NOT_EXISTS.get_response()
  test_data = get_test_id_in_table(test_id)
  return {'skeleton': test_data}, 200


@skeleton_bp.route('/skeleton', methods=['POST'])
@use_kwargs(RequestBodySchema)
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="skeleton post",
     description="skeleton post")
def skeleton_post(**kwargs):
  test_id = kwargs.get('id', None)
  test_name = kwargs.get('name', None)
  test_count = kwargs.get('count', None)
  if None in [test_id, test_name, test_count]:
    return ERROR_BODY_NOT_EXISTS.get_response()
  if check_test_id_exists(test_id):
    return ERROR_ID_ALREADY_EXISTS.get_response()
  insert_test_id_in_table(test_id, test_name, test_count)
  return SUCCESS_ID_INSERT.get_response()


@skeleton_bp.route('/skeleton', methods=['PUT'])
@use_kwargs(RequestBodySchema)
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="skeleton put",
     description="skeleton put")
def skeleton_put(**kwargs):
  test_id = kwargs.get('id', None)
  test_name = kwargs.get('name', None)
  test_count = kwargs.get('count', None)
  if None in [test_id, test_name, test_count]:
    return ERROR_BODY_NOT_EXISTS.get_response()
  if not check_test_id_exists(test_id):
    return ERROR_ID_NOT_EXISTS.get_response()
  update_test_id_in_table(test_id, test_name, test_count)
  return SUCCESS_ID_UPDATE.get_response()


@skeleton_bp.route('/skeleton', methods=['DELETE'])
@use_kwargs(RequestParameterSchema, locations=("querystring"))
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="skeleton delete",
     description="skeleton delete")
def skeleton_delete(**kwargs):
  test_id = kwargs.get('id', None)
  if test_id is None:
    return ERROR_PARAMETER_NOT_EXISTS.get_response()
  if not check_test_id_exists(test_id):
    return ERROR_ID_NOT_EXISTS.get_response()
  delete_test_id_in_table(test_id)
  return SUCCESS_ID_DELETE.get_response()
