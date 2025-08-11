from flask import Flask
from dotenv import load_dotenv
import os, secrets


class Config:
    load_dotenv()
    DEBUG = True
    SECRET_KEY = secrets.token_hex(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False