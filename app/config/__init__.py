from flask import Flask
from dotenv import load_dotenv
import os


class Config:
    load_dotenv()
    DEBUG = os.getenv('DEBUG', '1') == '1'
    SECRET_KEY = os.getenv('SECRET_KEY', None)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False