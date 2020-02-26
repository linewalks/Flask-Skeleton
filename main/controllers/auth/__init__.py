from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix="/api")

API_CATEGORY = 'Auth'

authorization_header = {
    "Authorization": {
        "description":
        "Authorization HTTP header with JWT access token, like: Authorization: Bearer asdf.qwer.zxcv",
        "in":
        "header",
        "type":
        "string",
        "required":
        True
    }
}

from .user import *
