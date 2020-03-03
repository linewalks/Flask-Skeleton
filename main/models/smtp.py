# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText


class Smtp:

  def __init__(self, server_ip, server_port):
    self.server_ip = server_ip
    self.server_port = server_port

  def connect(self):
    self.s = smtplib.SMTP(self.server_ip, self.server_port)

  def disconnect(self):
    self.s.quit()

  def set_account(self, emailid, password):
    self.emailid = emailid
    self.password = password

  def login(self):
    self.s.ehlo()
    self.s.starttls()
    self.s.login(self.emailid, self.password)

  def sendmail(self, to_email, msg):
    message = MIMEText(msg.body, "html", _charset="utf-8")
    message["Subject"] = msg.title
    message["From"] = self.emailid
    message["To"] = to_email
    self.connect()
    self.login()
    self.s.sendmail(self.emailid, to_email, message.as_string())
    self.disconnect()

  def close(self):
    self.s.close()
