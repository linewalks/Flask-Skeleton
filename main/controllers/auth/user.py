from flask import current_app as apispec
from flask_apispec import use_kwargs, marshal_with, doc
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token,
    get_jwt
)
from main.controllers.auth import auth_bp, API_CATEGORY, authorization_header
from main import db, jwt, email_sender
from main.models.resources import (
    ResponseLoginSchema,
    RequestLoginSchema,
    ResponseBodySchema,
    ResponseAccessTokenSchema,
    RequestEmailVerification
)
from main.models.mail import SignupCheck
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
    ERROR_SIGNUP_VERIFICATION,
    ERROR_SEND_MAIL,
    SUCCESS_SIGNUP,
    SUCCESS_LOGOUT,
    SUCCESS_VERIFICATION
)


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_payload):
  jti = jwt_payload["jti"]
  return TokenBlacklist.is_token_revoked(jti)


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
  if not u.confirmed:
    return ERROR_NOT_VALIDATED_ACCOUNT.get_response()
  return u.to_dict()


@auth_bp.route('/verify_email', methods=['GET'])
@use_kwargs(RequestEmailVerification)
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="사용자 이메일 확인",
     description="사용자의 이메일을 확인합니다")
def verify_email(**kwargs):
  email = kwargs["email"]
  if not User.exists(email):
    return ERROR_USER_NOT_EXISTS.get_response()

  u = User.get_info(email)
  if u.token != kwargs["token"]:
    return ERROR_SIGNUP_VERIFICATION.get_response()
  else:
    u.confirmed = True
    db.session.commit()
    return SUCCESS_VERIFICATION.get_response()


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
  try:
    email_sender.sendmail(user_info.email, SignupCheck(user_info))
  except Exception as e:
    return ERROR_SEND_MAIL.get_response()

  return SUCCESS_SIGNUP.get_response()


@auth_bp.route("/signout", methods=["POST"])
@jwt_required
@marshal_with(ResponseError)
@doc(tags=[API_CATEGORY],
     summary="로그아웃",
     description="사용자 로그아웃을 합니다.",
     params=authorization_header)
def signout():
  TokenBlacklist.revoke_token(get_jwt(), app.config["JWT_IDENTITY_CLAIM"])
  return SUCCESS_LOGOUT.get_response()


@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
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

