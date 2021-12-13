from flask import current_app as app
from urllib.parse import urlencode

from main.models.user import User


class EmailMessage(object):
  def __init__(self):
    self.title_prefix = "[회원가입 인증메일]"
    self.site_url = app.config["SITE_URI"]


class SignupCheck(EmailMessage):
  def __init__(self, user, **kwargs):
    super(SignupCheck, self).__init__()
    self.default_title = "계정 인증 안내"
    self.user_info = urlencode(user.to_dict_email_verification())
    self.url = f"{self.site_url}/api/verify_email?{self.user_info}"
    self.default_body = f"""
    <p>회원가입 인증메일입니다</p>

    <p>아래 링크를 클릭하여 이메일을 인증해주시기 바랍니다.</p>
    <p><a href="{self.url}" target="_blank">이메일 확인</a>
    """

  @property
  def title(self):
    return f"{self.title_prefix} {self.default_title}"

  @property
  def body(self):
    return self.default_body
