from flask import Blueprint
from flask_restful import Api

from .school_controller import SchoolController


# Api routes registration for operation area
bp = Blueprint("backoffice_api", __name__, url_prefix="/backoffice")
api = Api(bp)
api.add_resource(SchoolController, "/school/")


def init_app(app):
    app.register_blueprint(bp)
