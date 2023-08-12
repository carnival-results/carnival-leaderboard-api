from flask import Blueprint
from flask_restful import Api

from .school_controller import SchoolController
from .leaderboard_controller import LeaderboardController


# Main application API
bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(bp)
api.add_resource(LeaderboardController, "/leaderboard/")

# Api routes for operation area
backoffice_bp = Blueprint("backoffice_api", __name__, url_prefix="/backoffice")
backoffice_api = Api(bp)
backoffice_api.add_resource(SchoolController, "/school/")


# Healthcheck and app version routes
system_bp = Blueprint("system", __name__)


@system_bp.route("/healthcheck")
def health():
    return "SERVER_IS_READ"


def init_app(app):
    app.register_blueprint(bp)
    app.register_blueprint(backoffice_bp)
    app.register_blueprint(system_bp)
