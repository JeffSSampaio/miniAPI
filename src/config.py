from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

base = os.path.abspath(os.path.dirname(__file__))
instance = os.path.join(base, './instance')
os.makedirs(instance, exist_ok=True)
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(instance, 'api.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''
    DEBUG = True