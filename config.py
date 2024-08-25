import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  HOST = str(os.environ.get("DB_HOST"))
  DATABASE = str(os.environ.get("DB_DATABASE"))
  USERNAME = str(os.environ.get("DB_USERNAME"))
  PASSWORD = str(os.environ.get("DB_PASSWORD"))