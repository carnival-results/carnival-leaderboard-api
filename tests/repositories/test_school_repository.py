import pytest
from mongomock import MongoClient
from unittest.mock import Mock

from src.repositories.school_repository import SchoolRepository


@pytest.fixture(autouse=True)
def mock_create_mongo_connection(mocker):
    return mocker.patch(
        "src.repositories.school_repository.create_mongo_connection",
        return_value=MongoClient().db["school"],
    )


def test_create_school_repository():
    data = {"name": "Pandas School", "city": "Santos"}

    repo = SchoolRepository()
    school_id = repo.create(data)

    assert school_id is not None
