from flask import Flask, render_template


def register(app: Flask):

    @app.route("/")
    def home():
        return render_template("index.html")