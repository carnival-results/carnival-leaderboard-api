from src.db import create_mongo_connection
from src.entities import School


class SchoolRepository:
    def __init__(self):
        self.school_collection = create_mongo_connection("schools")

    def create(self, data):
        school_data = self._mapper(data)
        school = self.school_collection.insert_one(school_data)

        return str(school.inserted_id)

    def _mapper(self, data):
        return School(data.get("name"), data.get("city")).__dict__
