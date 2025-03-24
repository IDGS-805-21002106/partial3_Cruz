import os 
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY=''
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:4771564924@localhost/Login'
    SQLALCHEMY_TRACK_MODIFICATIONS = False