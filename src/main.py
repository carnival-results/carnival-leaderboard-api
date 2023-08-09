import os
from flask import Flask

import config
import controllers


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    controllers.init_app(app)

    return app


app = create_app()


@app.route("/health")
def health():
    return "SERVER_IS_READ"
