import os
from flask import Flask

from src import config, controllers


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    controllers.init_app(app)

    return app


app = create_app()
