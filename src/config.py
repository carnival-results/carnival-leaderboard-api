import os
from dotenv import load_dotenv
from flask_cors import CORS


class ApplicationConfig:
    FLASK_APP = os.getenv("FLASK_APP")


def init_app(app):
    load_dotenv()
    app.config.from_object(ApplicationConfig)
    CORS(
        app,
        resources={r"/api/*": {"origins": os.getenv("MAIN_APP_URL")}},
        supports_credentials=True,
    )
