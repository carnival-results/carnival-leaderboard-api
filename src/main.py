from flask import Flask

import config


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    return app


# For running the project with gunicorn
app = create_app()


@app.route("/health")
def health():
    return "SERVER_IS_READ"
