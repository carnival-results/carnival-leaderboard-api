from flask import request, jsonify
from flask_restful import Resource

from src.usecases.school_usecase import CreateSchool
from src.repositories.school_repository import SchoolRepository


repository = SchoolRepository()


class SchoolController(Resource):
    def post(self):
        data = request.json

        create_school_usecase = CreateSchool(repository)
        school = create_school_usecase.execute(data)

        response = jsonify(school)
        response.status_code = 201
        return response
