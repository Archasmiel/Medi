from flask import Flask
from flask_migrate import Migrate
from app.services.database import db

migrate = Migrate()


def register(app: Flask):
    migrate.init_app(app, db)