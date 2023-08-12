from flask import Blueprint
from flask_restful import Api

from .school_controller import SchoolController


# Api routes registration for operation area
bp = Blueprint("backoffice_api", __name__, url_prefix="/backoffice")
api = Api(bp)
api.add_resource(SchoolController, "/school/")

# Healthcheck and app version routes
system_bp = Blueprint("system", __name__)


@system_bp.route("/healthcheck")
def health():
    return "SERVER_IS_READ"


def init_app(app):
    app.register_blueprint(bp)
    app.register_blueprint(system_bp)
