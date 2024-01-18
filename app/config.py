import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    # Admin credentials
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "admin"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/msuchatbot"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
