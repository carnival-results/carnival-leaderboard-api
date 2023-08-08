import os


class ApplicationConfig:
    FLASK_APP = "src/main.py"


def init_app(app):
    app.config.from_object(ApplicationConfig)
