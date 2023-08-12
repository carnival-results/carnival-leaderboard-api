from flask import jsonify
from flask_restful import Resource

from src.usecases.leaderboard_usecase import GetLeaderboard


class LeaderboardController(Resource):
    def get(self):
        leaderboard = GetLeaderboard()
        response = jsonify(leaderboard.execute())

        return response
