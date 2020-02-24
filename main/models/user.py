from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    decode_token
)
import random
import string
import base64a
from .. import app, db


def randomStringDigits(string_length=16):
  """Generate a random string of letters and digits """
  letters = string.printable
  rand_password = [random.choice(letters)
                   for _ in range(string_length)]
  random.shuffle(rand_password)
  return "".join(rand_password)


class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(64), unique=True, index=True)
  password_hash = db.Column(db.String(128))
  token = db.Column(db.String(64))
  token_created_time = db.Column(db.DateTime, default=datetime.utcnow)

  def convert_password_to_hash(self, password):
    self.password_hash = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.password_hash, password)

  def generate_token(self, created_time):

    string_to_encrypt = "name:{name},created_time:{created_time}".format(
        name=self.name,
        created_time=created_time.strftime("%Y-%m-%d %H-%M-%S")
    )

    token = base64.b64encode(app.crypto.encrypt(str.encode(string_to_encrypt)))
    return token.decode("utf-8", "ignore")

  def generate_access_token(self):
    return create_access_token(identity=dict(email=self.email,
                                             name=self.name))

  def generate_refresh_token(self):
    return create_refresh_token(identity=dict(email=self.email,
                                              name=self.name))

  @staticmethod
  def exists(email):
    return User.query.filter(User.email == email).scalar()

  @staticmethod
  def verified(email):
    u = User.query.filter(User.email == email).one_or_none()
    return u.confirmed if u else False

  @staticmethod
  def get_info(email):
    return User.query.filter(User.email == email).first()

  @staticmethod
  def delete(email):
    User.query.filter(User.email == email).delete()

  @staticmethod
  def random_password():
    return randomStringDigits()