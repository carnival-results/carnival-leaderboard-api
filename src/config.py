import os
from dotenv import load_dotenv


class ApplicationConfig:
    FLASK_APP = os.getenv("FLASK_APP")


def init_app(app):
    # Load environment variables from .env file
    load_dotenv()
    app.config.from_object(ApplicationConfig)
