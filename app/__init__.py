from flask import Flask
from .routes import register as route_register
from .services import register as service_register
from .config import DevConfig, ProdConfig

def create_app():
    app = Flask(__name__,
                static_folder='../static',
                template_folder='../templates')

    app.config.from_object(DevConfig)
    service_register(app)
    route_register(app)

    return app