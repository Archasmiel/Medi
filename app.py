from flask import Flask, render_template
from api.routes import register as route_register

if __name__ == "__main__":
    app = Flask(__name__)
    route_register(app)
    app.run(debug=True)