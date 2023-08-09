from db import create_mongo_client
from entities import School


class SchoolRepository:
    def __init__(self):
        self.db = create_mongo_client()
        self.school_collection = self.db["schools"]

    def create(self, data):
        school_data = self._mapper(data)
        school = self.school_collection.insert_one(school_data)

        return str(school.inserted_id)

    def _mapper(self, data):
        return School(data.get("name"), data.get("city")).__dict__
