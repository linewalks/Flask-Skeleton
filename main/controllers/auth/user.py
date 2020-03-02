from flask_apispec import use_kwargs, marshal_with, doc
from flask_jwt_extended import (jwt_required,
                                jwt_refresh_token_required,
                                get_jwt_identity,
                                create_access_token,
                                get_raw_jwt)
from main.controllers.auth import auth_bp, API_CATEGORY, authorization_header
from main import app, db, jwt
from main.models.resources import ResponseLoginSchema, RequestLoginSchema, ResponseBodySchema, ResponseAccessTokenSchema
from main.models.user import User, TokenBlacklist
from main.models.common.error import (
    ResponseError,
    ERROR_NULL_EMAIL,
    ERROR_NULL_PASSWORD,
    ERROR_USER_EMAIL_EXISTS,
    ERROR_USER_EMAIL_NOT_EXISTS,
    ERROR_VERIFY_EMAIL_PASSWORD,
    ERROR_USER_NOT_EXISTS,
    ERROR_NOT_VALIDATED_ACCOUNT,
    SUCCESS_SIGNUP,
    SUCCESS_LOGOUT
)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decoded_token):
    return TokenBlacklist.is_token_revoked(decoded_token)


@auth_bp.route('/signin', methods=['POST'])
@use_kwargs(RequestLoginSchema)
@marshal_with(ResponseLoginSchema, code=200)
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="로그인",
     description="사용자 로그인을 합니다")
def signin(**kwargs):
  email = kwargs.get('email', None)
  password = kwargs.get('password', None)
  if not email:
    return ERROR_NULL_EMAIL.get_response()
  if not password:
    return ERROR_NULL_PASSWORD.get_response()
  if not User.exists(email):
    return ERROR_USER_EMAIL_NOT_EXISTS.get_response()
  u = User.get_info(email)
  if not u.verify_password(password):
    return ERROR_VERIFY_EMAIL_PASSWORD.get_response()
  return u.to_dict()


@auth_bp.route('/signup', methods=['POST'])
@use_kwargs(RequestLoginSchema)
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="회원가입",
     description="사용자 회원가입을 합니다")
def signup(**kwargs):
  email = kwargs.get('email', None)
  password = kwargs.get('password', None)
  if User.exists(email):
    return ERROR_USER_EMAIL_EXISTS.get_response()
  user_info = User(**kwargs)
  db.session.add(user_info)
  db.session.commit()
  return SUCCESS_SIGNUP.get_response()


@auth_bp.route("/signout", methods=["POST"])
@jwt_required
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="로그아웃",
     description="사용자 로그아웃을 합니다.",
     params=authorization_header)
def signout():
  TokenBlacklist.revoke_token(get_raw_jwt(), app.config["JWT_IDENTITY_CLAIM"])
  return SUCCESS_LOGOUT.get_response()


@auth_bp.route("/refresh", methods=["POST"])
@jwt_refresh_token_required
@marshal_with(ResponseAccessTokenSchema, code=200)
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="access 토큰 갱신",
     description="access 토큰을 갱신합니다.",
     params=authorization_header)
def refresh():
  current_user = get_jwt_identity()
  if not User.exists(current_user["email"]):
      return ERROR_USER_NOT_EXISTS.get_response()
  access_token = create_access_token(identity=dict(email=current_user["email"]))
  TokenBlacklist.add_token_to_database(access_token, app.config["JWT_IDENTITY_CLAIM"])
  return {"access_token": access_token}
